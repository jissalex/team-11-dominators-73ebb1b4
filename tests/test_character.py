from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterLessThanTwoLetters(TestCase):
    def test_init(self):
        ARBITARYY_LENGTH = "4"
        testobj = Character(ARBITARY_LENGTH)
        self.assertEqual(ARBITARYY_LENGTH, testobj.length)

#create fake map underneath this