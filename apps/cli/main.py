import sys
import os
import time
from pathlib import Path
sys.path.append(str(Path(__file__).parents[2]))

from src.ngrok_support import connect_ngrok, disconnect_ngrok
from src.ngrok_support.config import NGROK_AUTH_TOKEN, LOCAL_PORT, LOCAL_HOST, TUNNEL_TYPE


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Connect to ngrok tunnel")
    parser.add_argument("--port", type=int, default=LOCAL_PORT, help=f"Local port to tunnel (default: {LOCAL_PORT})")
    parser.add_argument("--host", default=LOCAL_HOST, help=f"Local host (default: {LOCAL_HOST})")
    parser.add_argument("--auth-token", default=NGROK_AUTH_TOKEN, help="ngrok auth token")
    parser.add_argument("--type", default=TUNNEL_TYPE, choices=["http", "tcp", "tls"], help=f"Tunnel type (default: {TUNNEL_TYPE})")
    parser.add_argument("--bind-host", default=LOCAL_HOST, help="Bind tunnel to a specific host/interface")
    parser.add_argument("--disconnect", action="store_true", help="Disconnect all tunnels")
    args = parser.parse_args()

    print(f"Config: port={args.port} host={args.host} type={args.type} bind_host={args.bind_host or '(none)'}")

    if args.disconnect:
        disconnect_ngrok()
        print("Disconnected all ngrok tunnels.")
    else:
        url = connect_ngrok(
            addr=args.port,
            proto=args.type,
            host_header=f"{args.host}:{args.port}",
            auth_token=args.auth_token,
            bind_host=args.bind_host or None,
        )
        print(f"Your service is now accessible at: {url}")
        print("Press Ctrl+C to stop...")
        try:
            start = time.time()
            while True:
                time.sleep(1)
                elapsed = int(time.time() - start)
                mins, secs = divmod(elapsed, 60)
                print(f"\rTime elapsed: {mins:02d}:{secs:02d}   ", end="", flush=True)
                        
        except KeyboardInterrupt:
            print("\nStopping ngrok...")
            disconnect_ngrok()
