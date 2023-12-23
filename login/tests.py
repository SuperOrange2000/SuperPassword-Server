from django.test import TestCase
from login.models import *
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        u = User.objects.create(
            username = "testName",
        )
        aes_key = hashlib.sha256((u.solt + "0000").encode()).digest()
        encryptor = Cipher(algorithms.AES(aes_key), modes.CBC(u.iv)).encryptor()
        u.check_code = encryptor.update(b'\x10'*algorithms.AES.block_size)+encryptor.finalize()
        u.save()
    
    def test_repeat_create(self):
        print("create")