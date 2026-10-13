# passgen

Make cryptographically secure passwords in python 

## Install

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```
uv tool install git+https://github.com/jaryaman/passgen@master
```

## Usage

```
$ passgen
$ passgen -n 32
$ passgen --no-punct
$ passgen --words
$ passgen --words 8
```

A cryptographically strong password is printed.

`--words` prints a passphrase of random dictionary words (7 by default), which is easier to memorise and type.
Each word adds about 12.9 bits of entropy, so 7 words give about 90 bits.

It can also be used from python:

```python
from passgen import make_password, make_passphrase
make_password()
make_passphrase()
```

## Development

```
uv sync
uv run pytest
```

## Wordlist

The words come from the [EFF large wordlist](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)
by the Electronic Frontier Foundation, used under [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/).
