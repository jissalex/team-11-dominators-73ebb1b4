
class Character:
    name = "Fire"
    current_position = 100 

    def __init__(self, character_name):
      self.name = character_name

    def enter_map(self, map):
        pass
    
    def get_Name(self):
        return self.name
    
    def get_Position(self):
        return self.current_position


##copied from Level-Up-Sync
from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

class Character:
    name = ""
    current_position :Position = Position(-100,-100)
    map :Map = Map()

    def __init__(self, character_name):
        self.name = character_name

    def move(self, direction :Direction) -> None:
        self.current_position = self.map.calculate_new_position(
            self.current_position, direction)
    
    def enter_map(self, map :Map):
        self.map = map
        self.current_position = self.map.starting_position