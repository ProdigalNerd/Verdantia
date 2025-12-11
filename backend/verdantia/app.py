from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
from .ws_protocol import Envelope, PROTOCOL_VERSION

app = FastAPI(title="Verdantia Backend")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in list(self.active_connections):
            try:
                await connection.send_json(message)
            except Exception:
                self.disconnect(connection)

manager = ConnectionManager()

@app.get("/")
async def root():
    return {"status": "ok", "service": "verdantia-backend"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            # Basic protocol validation
            if isinstance(data, dict) and data.get("v") == PROTOCOL_VERSION:
                # Echo back for now
                await manager.broadcast({"v": PROTOCOL_VERSION, "type": "echo", "id": data.get("id"), "payload": data.get("payload")})
            else:
                await websocket.send_json({"v": PROTOCOL_VERSION, "type": "error", "id": None, "payload": {"message": "protocol mismatch"}})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
