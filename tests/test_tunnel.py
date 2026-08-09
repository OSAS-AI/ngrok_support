from unittest.mock import patch

import pytest

from src.ngrok_support.tunnel import connect_ngrok, disconnect_ngrok


class TestConnectNgrok:
    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_kills_existing_process(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434)
        mock_ngrok.kill.assert_called_once_with()

    @patch("src.ngrok_support.tunnel.ngrok")
    @patch("src.ngrok_support.tunnel.conf")
    def test_connect_sets_auth_token(self, mock_conf, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, auth_token="my_token")
        assert mock_conf.get_default.return_value.auth_token == "my_token"

    @patch("src.ngrok_support.tunnel.ngrok")
    @patch("src.ngrok_support.tunnel.conf")
    def test_connect_skips_auth_when_none(self, mock_conf, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, auth_token=None)
        mock_conf.get_default.assert_not_called()

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_returns_public_url(self, mock_ngrok):
        expected = "https://abc.ngrok.io"
        mock_ngrok.connect.return_value.public_url = expected
        result = connect_ngrok(addr=11434)
        assert result == expected

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_passes_connect_kwargs(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, proto="http", host_header="localhost:11434")
        mock_ngrok.connect.assert_called_once_with(
            addr=11434, proto="http", host_header="localhost:11434"
        )

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_with_bind_host(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, bind_host="192.168.1.1")
        mock_ngrok.connect.assert_called_once_with(
            addr="192.168.1.1:11434", proto="http", host_header="localhost:11434"
        )

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_skips_bind_host_for_localhost(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, bind_host="localhost")
        mock_ngrok.connect.assert_called_once_with(
            addr=11434, proto="http", host_header="localhost:11434"
        )

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_skips_bind_host_for_loopback(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, bind_host="127.0.0.1")
        mock_ngrok.connect.assert_called_once_with(
            addr=11434, proto="http", host_header="localhost:11434"
        )

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_skips_bind_host_when_empty(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(addr=11434, bind_host="")
        mock_ngrok.connect.assert_called_once_with(
            addr=11434, proto="http", host_header="localhost:11434"
        )


class TestDisconnectNgrok:
    @patch("src.ngrok_support.tunnel.ngrok")
    def test_disconnect_calls_ngrok(self, mock_ngrok):
        disconnect_ngrok()
        mock_ngrok.kill.assert_called_once_with()
