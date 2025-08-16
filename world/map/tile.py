class Tile():
    def __init__(self, x, y, elevation, type):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.type = type

    def get_elevation(self):
        return self.elevation
