class Tile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = "grass"
        self.elevation = 0.0

    def set_elevation(self, elevation):
        self.elevation = elevation
