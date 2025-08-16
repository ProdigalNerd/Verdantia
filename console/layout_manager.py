from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table

from world.map.tile_type import TILE_TYPES

console = Console()

class LayoutManager():
    def __init__(self):
        pass

    def render_layout(self, map, stats):
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="body"),
        )
        layout["header"].update(Panel("[bold magenta]My World Simulation[/]"))
        layout["body"].split_row(
            Layout(self.__render_hud__(stats), name="hud", size=30),
            Layout(self.__render_map__(map), name="map"),
        )
        return layout
    
    def __render_map__(self, map):
        table = Table.grid(padding=0)
        for row in map:
            cells = []
            for tile in row:
                color, symbol = TILE_TYPES.get(tile.type, ("white", "?"))
                cells.append(f"[{color}]{symbol}[/]")
            table.add_row(*cells)
        return table

    def __render_hud__(self, stats):
        pass