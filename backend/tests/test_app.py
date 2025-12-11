from fastapi.testclient import TestClient
from verdantia.app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("service") == "verdantia-backend"


def test_websocket_echo():
    with client.websocket_connect("/ws") as ws:
        msg = {"v": 1, "type": "ping", "id": "1", "payload": {"message": "hello"}}
        ws.send_json(msg)
        data = ws.receive_json()
        assert data.get("type") == "echo"
        assert data.get("payload") == msg["payload"]
