import os
from pathlib import Path
from dotenv import load_dotenv

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DOTENV_PATH = _PROJECT_ROOT / "secrets" / ".env"

load_dotenv(_DOTENV_PATH)


def get_config(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)


NGROK_AUTH_TOKEN: str = get_config("NGROK_AUTH_TOKEN", "")
LOCAL_HOST: str = get_config("LOCAL_TUNNEL_HOST", "127.0.0.1")
LOCAL_PORT: int = int(get_config("LOCAL_TUNNEL_PORT", "11434"))
TUNNEL_TYPE: str = get_config("TUNNEL_TYPE", "http")
