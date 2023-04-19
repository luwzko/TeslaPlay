import yaml

class Settings:
    def __init__(self, file):
        self.settings_file = open(file)
        self.content = yaml.safe_load(self.settings_file)
    # return whole settings.yaml dictionary
    def get_content(self) -> dict:
        return self.content
    # return tuple (id, game)
    def get_games(self) -> list:
        for k in self.content:
            yield (k, self.content[k])
    # return game by id
    def get_game_by_id(self, _id) -> list:
        return self.content[_id]
    # destructor
    def __del__(self):
        self.settings_file.close()