class TickController():
    def __init__(self):
        self.ticks = 0
        self.modules = []

    def register(self, module):
        self.modules.append(module)

    def process_tick(self):
        for module in self.modules:
            module.update()
        self.ticks += 1