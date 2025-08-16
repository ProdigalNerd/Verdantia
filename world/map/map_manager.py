import os

from world.map.perlin_noise_map import PerlinNoise
from world.map.tile import Tile


class MapManager():
    tiles = []

    def __init__(self):
        width = int(os.getenv("MAP_WIDTH") or 10)
        height = int(os.getenv("MAP_HEIGHT") or 10)
        self.tiles = [[self.__generate_tile__(x, y) for x in range(width)] for y in range(height)]
        self.perlin_noise = PerlinNoise(width, height)

    def __generate_tile__(self, x, y):
        tile = Tile(x, y)
        tile.set_elevation(self.perlin_noise.get_value(x, y))
        self.tiles[x][y] = tile
