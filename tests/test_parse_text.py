import pytest

from main import parse_text


@pytest.mark.parametrize("text,expected", [
    ("Hello world.", (2, 1)),
    ("There are many types of sentences, all with different structures and complexities. In its most basic form, a sentence is made up of a subject and predicate, which is the verb and the words that follow. But no matter how simple or complex, a sentence consists of words. Words in a sentence are what make it come alive and make sense.", (61, 4)),
    ("I don't want anything to drink.", (6, 1)),
    ("Hello world... I don't want anything to drink! Can you go away?", (12, 3)),
    ("Подальші два роки запам’яталися встановленням нових рекордів, адже́ кількість учасників збільшилася вдвічі. До речі, дюк де Рішельє також долучається до цієї події. Четвертий рік поспіль святковий гардероб герцога поповнюється найрізноманітнішими виши́ванками: блакитно-синій і яскраво-червоний, жовтогарячий і ніжно-зелений – ось палітра його ви́шитих візерунків.", (43, 3))
])
def test_parse_text(text, expected):
    assert parse_text(text) == expected

