import asyncio
import websockets

clients = set()

async def handler(websocket):
    clients.add(websocket)
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received: {message}")
            msg = "Rohit is here to conquer the world"
            for client in clients:
                await client.send(f"Broadcast: {msg}")
    finally:
        clients.remove(websocket)
        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

asyncio.run(main())
