from unittest import TestCase
from levelup.controller import GameController

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Game Controller should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    
    def test_def_character(self):
        testObj = GameController()
        assert testObj.status.character_name == 'Character'

            
    def test_character(self):
        testObj = GameController()
        testObj.create_character('Fire')
        assert testObj.status.character_name == 'Fire'

    def test_def_pos(self):
        testObj = GameController()
        assert testObj.status.current_position == (-100,-100)
