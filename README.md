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
```

A cryptographically strong password is printed.

It can also be used from python:

```python
from passgen import make_password
make_password()
```

## Development

```
uv sync
uv run pytest
```
