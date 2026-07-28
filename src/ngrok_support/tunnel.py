from pyngrok import ngrok, conf


def connect_ngrok(addr: int = 11434,
                  proto: str = "http",
                  host_header: str = "localhost:11434",
                  auth_token: str | None = None,
                  bind_host: str | None = None) -> str:
    if auth_token:
        conf.get_default().auth_token = auth_token

    connect_kwargs = {
        "addr": addr,
        "proto": proto,
        "host_header": host_header,
    }

    if bind_host and bind_host not in ["localhost", ""]:
        if not bind_host.startswith(("http://", "https://")):
            bind_host = f"http://{bind_host}"
        connect_kwargs["bind_host"] = bind_host

    return ngrok.connect(**connect_kwargs).public_url


def disconnect_ngrok() -> None:
    ngrok.kill()


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
        url = connect_ngrok(addr=args.port)
        print(f"Your service is now accessible at: {url}")
