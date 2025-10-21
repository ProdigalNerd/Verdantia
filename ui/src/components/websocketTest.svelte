<script>
    const socket = new WebSocket('ws://localhost:8000/ws');

    socket.onopen = () => console.log("Connected!");
    socket.onmessage = (event) => {
        console.log(event.data);
        const data = JSON.parse(event.data);
        console.log("Tick update:", data);
    };

    function sendMove() {
        if (socket.readyState === WebSocket.OPEN) {
            socket.send(JSON.stringify({ type: "MOVE", entity_id: "p1", dir: "N" }));
        } else {
            console.log("WebSocket is not open.");
        }
    }
</script>

<h1>WebSocket Test</h1>
<button on:click={sendMove}>Send Move Command</button>
<button on:click={() => socket.close()}>Disconnect</button>
<button on:click={() => location.reload()}>Reconnect</button>