class GameManager:
    def __init__(self):
        self.tick_count = 0
        self.events = []
        self.world = {}
    
    def tick(self):
        self.tick_count += 1
        # do world updates here...
        self.events.append(f"Tick {self.tick_count}")
        return {"tick": self.tick_count, "events": self.events[-5:]}