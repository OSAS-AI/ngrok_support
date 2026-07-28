from unittest.mock import patch, MagicMock

import pytest

from src.ngrok_support.tunnel import connect_ngrok, disconnect_ngrok


class TestConnectNgrok:
    @patch("src.ngrok_support.tunnel.conf")
    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_sets_auth_token(self, mock_ngrok, mock_conf):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(port=11434, auth_token="my_token")
        mock_conf.get_default.return_value.auth_token = "my_token"

    @patch("src.ngrok_support.tunnel.conf")
    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_skips_auth_when_none(self, mock_ngrok, mock_conf):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(port=11434, auth_token=None)
        mock_conf.get_default.assert_not_called()

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_returns_public_url(self, mock_ngrok):
        expected = "https://abc.ngrok.io"
        mock_ngrok.connect.return_value.public_url = expected
        result = connect_ngrok(port=11434)
        assert result == expected

    @patch("src.ngrok_support.tunnel.ngrok")
    def test_connect_calls_with_correct_args(self, mock_ngrok):
        mock_ngrok.connect.return_value.public_url = "https://abc.ngrok.io"
        connect_ngrok(port=11434, proto="http", host_header="localhost:11434")
        mock_ngrok.connect.assert_called_once_with(11434, "http", host_header="localhost:11434")


class TestDisconnectNgrok:
    @patch("src.ngrok_support.tunnel.ngrok")
    def test_disconnect_calls_ngrok(self, mock_ngrok):
        disconnect_ngrok()
        mock_ngrok.disconnect.assert_called_once_with()
