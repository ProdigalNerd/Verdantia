from pydantic import BaseModel
from typing import Any, Optional
from uuid import UUID

class Envelope(BaseModel):
    v: int
    type: str
    id: Optional[str]
    payload: Any

PROTOCOL_VERSION = 1
