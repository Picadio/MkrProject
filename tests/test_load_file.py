import sys

import pytest

from main import load_file


@pytest.mark.parametrize("file_path,expected", [
    ("test_files/test.txt", "I don't want anything to drink."),
    ("test_files/test2.txt", "Simply type in the word you want to explore the meaning of and find your screen filled with countless examples of that word in a sentence."),
    ("test_files/test3.txt", "There are many types of sentences, all with different structures and complexities. In its most basic form, a sentence is made up of a subject and predicate, which is the verb and the words that follow. But no matter how simple or complex, a sentence consists of words. Words in a sentence are what make it come alive and make sense.")
])
def test_load_file(file_path, expected):
    assert load_file(file_path) == expected

