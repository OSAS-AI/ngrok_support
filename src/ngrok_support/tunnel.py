from pyngrok import ngrok, conf


def connect_ngrok(port: int = 11434, 
                  proto: str = "http", 
                  host_header: str = "localhost:11434", 
                  auth_token: str | None = None) -> str:
    if auth_token:
        conf.get_default().auth_token = auth_token
    return ngrok.connect(port, proto, host_header=host_header).public_url


def disconnect_ngrok() -> None:
    ngrok.disconnect()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=11434)
    parser.add_argument("--disconnect", action="store_true")
    args = parser.parse_args()
    if args.disconnect:
        disconnect_ngrok()
        print("Disconnected all ngrok tunnels.")
    else:
        url = connect_ngrok(port=args.port)
        print(f"Your service is now accessible at: {url}")
