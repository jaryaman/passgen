import string

import pytest
from passgen import WORDS, main, make_passphrase, make_password

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


def test_wordlist_is_the_full_eff_large_list():
    # 7776 = 6^5 distinct words is what gives 12.9 bits of entropy per word
    assert len(WORDS) == 7776
    assert len(set(WORDS)) == 7776
    assert WORDS[0] == 'abacus'
    assert WORDS[-1] == 'zoom'


def test_make_passphrase_default_is_seven_words_from_the_list():
    words = make_passphrase().split(' ')
    assert len(words) == 7
    assert set(words) <= set(WORDS)


def test_make_passphrase_word_count():
    assert len(make_passphrase(n=10).split(' ')) == 10


def test_make_passphrase_draws_across_the_list():
    # 2000 uniform draws from 7776 give about 1760 distinct words
    assert len(set(make_passphrase(n=2000).split(' '))) > 1500


def test_main_words_option_defaults_to_seven(capsys):
    main(['--words'])
    words = capsys.readouterr().out.rstrip('\n').split(' ')
    assert len(words) == 7
    assert set(words) <= set(WORDS)


def test_main_words_option_with_count(capsys):
    main(['--words', '9'])
    assert len(capsys.readouterr().out.rstrip('\n').split(' ')) == 9


def test_main_words_rejects_non_positive_count():
    with pytest.raises(SystemExit):
        main(['--words', '0'])


@pytest.mark.parametrize('conflicting', [['-n', '5'], ['--no-punct']])
def test_main_words_rejects_character_options(conflicting):
    with pytest.raises(SystemExit):
        main(['--words'] + conflicting)
