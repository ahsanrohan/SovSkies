from enemy import Enemy
import json





class LevelHandler():
    def __init__(self, *args, **kwargs):
        self.level_number = 0
        self.level_waves = []

        self.level_filepath = kwargs.get('filepath')    

    def get_level(self):
        level = json.load[level_filepath][self.level_number]
        for waves in level:
            pass


class waveHandler():

