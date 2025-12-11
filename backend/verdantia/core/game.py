from typing import Dict, List
from .entity import Entity

class Game:
    def __init__(self):
        self.entities: Dict[str, Entity] = {}

    def add_entity(self, entity: Entity):
        self.entities[entity.id] = entity

    def get_entity(self, entity_id: str) -> Entity:
        return self.entities.get(entity_id)

    def tick(self):
        # Advance world state; to be expanded
        pass
