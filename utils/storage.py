import hashlib
import os
from django.core.files import File, locks
from django.core.files.utils import validate_file_name
from django.core.files.storage import FileSystemStorage  
from django.core.files.move import file_move_safe
  
class HashStorage(FileSystemStorage):  
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)

    def save(self, name, content, max_length=None):
        """
        Save new content to the file specified by name. The content should be
        a proper File object or any Python file-like object, ready to be read
        from the beginning.
        """
        # Get the proper name for the file, as it will actually be saved.
        dirname = os.path.dirname(name)
        hash_value = hashlib.sha256(content.read()).hexdigest()
        name = os.path.join(dirname, f"{hash_value}.{name.split('.')[-1]}")

        if not hasattr(content, "chunks"):
            content = File(content, name)

        # name = self.get_available_name(name, max_length=max_length)
        name = self._save(name, content)
        # Ensure that the name returned from the storage system is still valid.
        validate_file_name(name, allow_relative_path=True)
        return name
    
    def _save(self, name, content):
        full_path = self.path(name)

        # Create any intermediate directories that do not exist.
        directory = os.path.dirname(full_path)
        try:
            if self.directory_permissions_mode is not None:
                # Set the umask because os.makedirs() doesn't apply the "mode"
                # argument to intermediate-level directories.
                old_umask = os.umask(0o777 & ~self.directory_permissions_mode)
                try:
                    os.makedirs(
                        directory, self.directory_permissions_mode, exist_ok=True
                    )
                finally:
                    os.umask(old_umask)
            else:
                os.makedirs(directory, exist_ok=True)
        except FileExistsError:
            raise FileExistsError("%s exists and is not a directory." % directory)

        # There's a potential race condition between get_available_name and
        # saving the file; it's possible that two threads might return the
        # same name, at which point all sorts of fun happens. So we need to
        # try to create the file, but if it already exists we have to go back
        # to get_available_name() and try again.

        try:
            # This file has a file path that we can move.
            if hasattr(content, "temporary_file_path"):
                file_move_safe(content.temporary_file_path(), full_path)

            # This is a normal uploadedfile that we can stream.
            else:
                # The current umask value is masked out by os.open!
                fd = os.open(full_path, self.OS_OPEN_FLAGS, 0o666)
                _file = None
                try:
                    locks.lock(fd, locks.LOCK_EX)
                    for chunk in content.chunks():
                        if _file is None:
                            mode = "wb" if isinstance(chunk, bytes) else "wt"
                            _file = os.fdopen(fd, mode)
                        _file.write(chunk)
                finally:
                    locks.unlock(fd)
                    if _file is not None:
                        _file.close()
                    else:
                        os.close(fd)
        except FileExistsError:
            pass

        if self.file_permissions_mode is not None:
            os.chmod(full_path, self.file_permissions_mode)

        # Ensure the saved path is always relative to the storage root.
        name = os.path.relpath(full_path, self.location)
        # Ensure the moved file has the same gid as the storage root.
        self._ensure_location_group_id(full_path)
        # Store filenames with forward slashes, even on Windows.
        return str(name).replace("\\", "/")