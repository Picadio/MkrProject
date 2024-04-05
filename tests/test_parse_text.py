import pytest

from main import parse_text


@pytest.mark.parametrize("text,expected", [
    ("Hello world.", (2, 1)),
    ("There are many types of sentences, all with different structures and complexities. In its most basic form, a sentence is made up of a subject and predicate, which is the verb and the words that follow. But no matter how simple or complex, a sentence consists of words. Words in a sentence are what make it come alive and make sense.", (61, 4)),
    ("I don't want anything to drink.", (6, 1))
])
def test_parse_text(text, expected):
    assert parse_text(text) == expected

