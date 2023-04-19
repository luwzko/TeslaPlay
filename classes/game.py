import os

class Game:
    def __init__(self, _id : int, game_name : str, game_path : str, description : str):
        self.id = _id
        self.game_name = game_name
        self.game_path = game_path
        self.description = description
        
    def run(self) -> None:
        os.startfile(self.game_path)