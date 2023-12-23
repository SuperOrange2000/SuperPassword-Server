import random
import string
from typing import Any

letters_and_digits = string.ascii_letters + string.digits

def random_string_func(length=32):
    return ''.join((random.choice(letters_and_digits) for i in range(length)))