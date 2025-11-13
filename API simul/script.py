import asyncio
import websockets
import json
import random
import time

async def send_fake_data(websocket):
    print(f"Client connecté : {websocket.remote_address}")
    heart = 70
    resp = 12

    try:
        while True:
            # Variation réaliste
            heart += random.uniform(-0.5, 0.5)
            resp += random.uniform(-0.2, 0.2)

            data = {
                "heart_rate": round(heart, 1),
                "resp_rate": round(resp, 1),
                "timestamp": time.time()
            }

            await websocket.send(json.dumps(data))
            await asyncio.sleep(0.1)  # 100 ms
    except websockets.exceptions.ConnectionClosed:
        print(f"Client déconnecté : {websocket.remote_address}")

async def main():
    async with websockets.serve(send_fake_data, "localhost", 8765):
        print("Serveur mock uRAD démarré sur ws://localhost:8765")
        await asyncio.Future()  # Tourne indéfiniment

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
