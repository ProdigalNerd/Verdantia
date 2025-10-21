import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from core.game_manager import GameManager
from contextlib import asynccontextmanager

game_manager = GameManager()
clients = set()

async def tick_engine():
    while True:
        print("Ticking the game engine...")
        diff = game_manager.tick()
        # Broadcast to connected clients
        for ws in list(clients):
            try:
                await ws.send_json(diff)
            except Exception:
                clients.remove(ws)
        await asyncio.sleep(1)  # tick rate = 1 tick/sec

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    task = asyncio.create_task(tick_engine())
    yield
    # shutdown
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def get():
    return HTMLResponse("""
    <html>
        <body>
            <h1>WebSocket Test</h1>
            <script>
                var ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) { alert(event.data); };
                ws.onopen = function() { ws.send("Hello Server!"); };
            </script>
        </body>
    </html>
    """)

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.add(ws)
    try:
        while True:
            action = await ws.receive_json()
            print(action)
            # Optionally, handle or respond to the action here
    except Exception:
        clients.remove(ws)

@app.websocket("/disconnect")
async def disconnect(ws: WebSocket):
    await ws.close()
    clients.remove(ws)