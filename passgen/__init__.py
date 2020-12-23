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
    character_space = string.ascii_uppercase + string.digits + string.ascii_lowercase
    if punct:
        character_space += string.punctuation

    password = ''.join(random.SystemRandom().choice(character_space) for _ in range(n))
    return password
