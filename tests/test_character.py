from unittest import TestCase
from levelup.character import Character

class Fakemap:
    pass

class FakePos:
    pass

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

#class TestCharacterLessThanTwoLetters(TestCase):
#   def test_init(self):
#        ARBITARY_LENGTH = "4"
#        testobj = Character(ARBITARY_LENGTH)
#        self.assertEqual(ARBITARY_LENGTH, testobj.length)
#create fake map underneath this

    def test_enter_map(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        fakemap = Fakemap()
        testobj.enter_map(fakemap)
        expected_position = 100
        self.assertEqual(testobj.current_position, expected_position)
    
    def test_get_name(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(testobj.get_Name(), 'MyName')

    def test_get_position(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(testobj.get_Position(), 100)

