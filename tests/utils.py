import random
import string


def generate_random_str(n):
    return ''.join(random.choices(string.ascii_letters, k=n))


def batch_assert(dict1, dict2, keys):
    for key in keys:
        assert dict1[key] == dict2[key]
