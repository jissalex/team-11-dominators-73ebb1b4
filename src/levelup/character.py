
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