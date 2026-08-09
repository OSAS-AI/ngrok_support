# ngrok_support

Expose local services via ngrok tunnels.

## Setup

```bash
pip install -r requirements/requirements.txt
```

Configure `secrets/.env`:

```env
NGROK_API_KEY=your_ngrok_auth_token
LOCAL_TUNNEL_HOST=127.0.0.1
LOCAL_TUNNEL_PORT=11434
TUNNEL_TYPE=http
```

## Usage

### CLI

```bash
python apps/cli/main.py
python apps/cli/main.py --port 8080
python apps/cli/main.py --port 8080 --host localhost --auth-token xxx --type http
python apps/cli/main.py --disconnect
```

### As a library

```python
from ngrok_support import connect_ngrok, disconnect_ngrok

url = connect_ngrok(port=11434, auth_token="xxx")
print(url)

disconnect_ngrok()
```

Run directly:

```bash
python -m src.ngrok_support.tunnel --port 11434
python -m src.ngrok_support.tunnel --disconnect
```

## Tests

```bash
pip install pytest
pytest tests/
```
