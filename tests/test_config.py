from src.ngrok_support.config import NGROK_AUTH_TOKEN, LOCAL_HOST, LOCAL_PORT, TUNNEL_TYPE, get_config


class TestConfigConstants:
    def test_ngrok_auth_token_is_str(self):
        assert isinstance(NGROK_AUTH_TOKEN, str)

    def test_local_host_is_str(self):
        assert isinstance(LOCAL_HOST, str)

    def test_local_port_is_int(self):
        assert isinstance(LOCAL_PORT, int)

    def test_tunnel_type_is_str(self):
        assert isinstance(TUNNEL_TYPE, str)


class TestGetConfig:
    def test_returns_default_when_key_missing(self):
        result = get_config("NONEXISTENT_KEY", "fallback")
        assert result == "fallback"

    def test_returns_none_when_no_default(self):
        result = get_config("NONEXISTENT_KEY")
        assert result is None
