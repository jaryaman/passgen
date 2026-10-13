"""Cryptographically strong password generation"""
import argparse
import random
import string
from pathlib import Path

# EFF large wordlist: 7776 words, so each word adds log2(7776) = 12.9 bits
WORDS = Path(__file__).with_name('eff_large_wordlist.txt').read_text().split()


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


def make_passphrase(n=7):
    """Make a passphrase of dictionary words

    Parameters
    ----------
    n: number of words

    Returns
    -------
    Space-separated words drawn from the EFF large wordlist with the highest quality random number sources
    provided by the operating system
    """
    return ' '.join(random.SystemRandom().choice(WORDS) for _ in range(n))


def _positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('must be at least 1')
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(prog='passgen', description=__doc__)
    parser.add_argument('-n', type=_positive_int, help='number of characters (default 20)')
    parser.add_argument('--no-punct', action='store_true', help='leave out punctuation characters')
    parser.add_argument('--words', type=_positive_int, nargs='?', const=7, metavar='N',
                        help='make a passphrase of N dictionary words instead (default 7)')
    args = parser.parse_args(argv)
    if args.words is None:
        print(make_password(n=args.n or 20, punct=not args.no_punct))
    elif args.n is not None or args.no_punct:
        parser.error('-n and --no-punct do not apply to --words')
    else:
        print(make_passphrase(n=args.words))
