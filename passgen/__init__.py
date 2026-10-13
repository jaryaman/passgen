"""Cryptographically strong password generation"""
import argparse
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


def _positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('must be at least 1')
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(prog='passgen', description=__doc__)
    parser.add_argument('-n', type=_positive_int, default=20, help='number of characters (default 20)')
    parser.add_argument('--no-punct', action='store_true', help='leave out punctuation characters')
    args = parser.parse_args(argv)
    print(make_password(n=args.n, punct=not args.no_punct))
