from dataclasses import dataclass, field
from typing import Dict, Any
import uuid

@dataclass
class Entity:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Unnamed"
    attributes: Dict[str, Any] = field(default_factory=dict)

    def apply_effect(self, effect: Dict[str, Any]):
        # Apply effect to entity attributes (simple merge)
        for k, v in effect.items():
            self.attributes[k] = self.attributes.get(k, 0) + v
