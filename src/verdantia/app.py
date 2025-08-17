from textual.app import App, ComposeResult
from textual.containers import Vertical

from .tick_controller import TickController
from world.world_manager import WorldManager

class VerdantiaApp(App):
    def __init__(self):
        super().__init__()
        self.world_manager = WorldManager()
        self.tick_controller = TickController()
        self.tick_controller.register(self.world_manager)

    def on_mount(self):
        self.set_interval(0.5, self.update) 

    def update(self):
        self.tick_controller.process_tick()

    def compose(self) -> ComposeResult:
        with Vertical():
            self.map_view = self.world_manager.get_map_view()
            # self.info_view = InfoView()
            yield self.map_view
            # yield self.info_view
    
    def on_key(self, event):
        if event.key == "q":
            self.exit()
        # elif event.key == "i":
            # self.info_view.visible = not self.info_view.visible

if __name__ == "__main__":
    VerdantiaApp().run()
