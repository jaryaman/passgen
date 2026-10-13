import string

import pytest
from passgen import main, make_password

ALPHANUMERIC = set(string.ascii_letters + string.digits)


def test_make_password_default_length():
    assert len(make_password()) == 20


def test_make_password_without_punctuation_is_alphanumeric():
    assert set(make_password(n=500, punct=False)) <= ALPHANUMERIC


def test_make_password_with_punctuation_uses_it():
    assert set(make_password(n=500)) & set(string.punctuation)


def test_main_prints_one_password(capsys):
    main([])
    out = capsys.readouterr().out
    assert out.endswith('\n')
    assert len(out.rstrip('\n')) == 20


def test_main_length_option(capsys):
    main(['-n', '32'])
    assert len(capsys.readouterr().out.rstrip('\n')) == 32


def test_main_no_punct_option(capsys):
    main(['-n', '500', '--no-punct'])
    assert set(capsys.readouterr().out.rstrip('\n')) <= ALPHANUMERIC


def test_main_rejects_non_positive_length():
    with pytest.raises(SystemExit):
        main(['-n', '0'])
