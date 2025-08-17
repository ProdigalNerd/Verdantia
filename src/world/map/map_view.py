from textual.widgets import Static
from rich.text import Text

from world.map.tile_type import TILE_TYPES

class MapView(Static):
    def __init__(self, map_manager):
        super().__init__()
        self.map_manager = map_manager

    def update_view(self):
        map = self.map_manager.get_map()
        text = Text()
        for row in map:
            for tile in row:
                tile_type = TILE_TYPES[tile.type]
                text.append(tile_type[1], style=tile_type[0])
            text.append("\n")
        self.update(text)