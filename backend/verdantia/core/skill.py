from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Skill:
    id: str
    name: str
    cost: int = 0
    cooldown: int = 0
    effects: Dict[str, Any] = None

    def apply(self, source, target):
        # Apply effects to target; real logic lives in handlers/plugins
        if self.effects:
            target.apply_effect(self.effects)
