import random
import string


def make_password(n=20):
    return ''.join(
        random.SystemRandom().choice(
            string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n)
    )
