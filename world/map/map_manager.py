import os

from world.map.perlin_noise import PerlinNoise
from world.map.tile import Tile
import random


class MapManager():
    def __init__(self):
        width = int(os.getenv("MAP_WIDTH") or 10)
        height = int(os.getenv("MAP_HEIGHT") or 10)
        random.seed(os.getenv("MAP_SEED") or 42)
        self.perlin_noise = PerlinNoise(width, height)
        self.current_settlement_count = 0
        self.max_settlements = 3
        self.tiles = [[self.__generate_tile__(x, y) for x in range(width)] for y in range(height)]

    def get_map(self):
        return self.tiles

    def __generate_tile__(self, x, y):
        elevation = self.perlin_noise.get_value(x, y)
        
        type = "grass"
        if elevation < 0:
            type = "water"
        elif self.__can_add_settlement__() and random.random() > 0.9995:
            type = "settlement"
            self.current_settlement_count += 1

        tile = Tile(x, y, elevation, type)
        return tile
    
    def __can_add_settlement__(self):
        if self.current_settlement_count < self.max_settlements:
            return True
        return False
