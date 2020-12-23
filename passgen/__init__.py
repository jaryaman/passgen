import random
import string


def make_password(n=20, punct=True):
    """Make a password

    Parameters
    ----------
    n: number of characters
    punct: with punctuation characters

    Returns
    -------
    A password generated with the highest quality random number sources provided by the operating system
    """
    if punct:
        password = ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(n)
        )
    else:
        password = ''.join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n)
        )
    return password
