from world.map.map_manager import MapManager


class WorldManager():
    def __init__(self):
        self.map_manager = MapManager()

    def update(self):
        # print("World is Updating")
        pass

    def get_map(self):
        return self.map_manager.get_map()
