from world.map.map_manager import MapManager
from world.map.map_view import MapView


class WorldManager():
    def __init__(self):
        self.map_manager = MapManager()
        self.map_view = MapView(self.map_manager)

    def update(self):
        self.map_view.update_view()

    def get_map(self):
        return self.map_manager.get_map()
    
    def get_map_view(self):
        return self.map_view
