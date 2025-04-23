import asyncio
import websockets

async def listen():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to server!")

        # Send a test message
        await websocket.send("Hello, this is a test message!")

        while True:
            message = await websocket.recv()
            print(f"Received: {message}")

asyncio.run(listen())
