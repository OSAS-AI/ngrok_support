from pyngrok import ngrok, conf


def connect_ngrok(addr: int = 11434,
                  proto: str = "http",
                  host_header: str = "localhost:11434",
                  auth_token: str | None = None,
                  bind_host: str | None = None) -> str:
    ngrok.kill()

    if auth_token:
        conf.get_default().auth_token = auth_token

    if bind_host and bind_host not in ["localhost", "127.0.0.1", ""]:
        addr = f"{bind_host}:{addr}"

    connect_kwargs = {
        "addr": addr,
        "proto": proto,
        "host_header": host_header,
    }

    return ngrok.connect(**connect_kwargs).public_url


def disconnect_ngrok() -> None:
    ngrok.kill()
