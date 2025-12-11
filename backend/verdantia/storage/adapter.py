from typing import Protocol, Any, Dict, Optional

class StorageAdapter(Protocol):
    async def init(self):
        ...

    async def get_player(self, player_id: str) -> Optional[Dict[str, Any]]:
        ...

    async def save_player(self, player_id: str, data: Dict[str, Any]):
        ...

# Placeholder adapters - implement with actual DB code later
class SQLiteAdapter:
    def __init__(self, url: str):
        self.url = url

    async def init(self):
        # initialize SQLite connection
        pass

    async def get_player(self, player_id: str):
        return None

    async def save_player(self, player_id: str, data: Dict[str, Any]):
        pass

class PostgresAdapter:
    def __init__(self, url: str):
        self.url = url

    async def init(self):
        # initialize asyncpg or sqlalchemy engine
        pass

    async def get_player(self, player_id: str):
        return None

    async def save_player(self, player_id: str, data: Dict[str, Any]):
        pass
