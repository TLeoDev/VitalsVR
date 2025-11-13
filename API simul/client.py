# python
import asyncio
import websockets
import json
import datetime

async def listen():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connecté à {uri}")
            while True:
                msg = await websocket.recv()
                try:
                    data = json.loads(msg)
                except json.JSONDecodeError:
                    print("Reçu (non-JSON):", msg)
                    continue

                ts = datetime.datetime.fromtimestamp(data.get("timestamp", 0)).isoformat()
                heart = data.get("heart_rate")
                resp = data.get("resp_rate")
                print(f"[{ts}] heart_rate={heart} bpm | resp_rate={resp} rpm")
    except (ConnectionRefusedError, OSError):
        print(f"Impossible de se connecter à {uri}. Vérifiez que le serveur tourne.")
    except websockets.exceptions.ConnectionClosed:
        print("Connexion fermée par le serveur.")

if __name__ == "__main__":
    try:
        asyncio.run(listen())
    except KeyboardInterrupt:
        print("\nArrêt demandé par l'utilisateur.")
