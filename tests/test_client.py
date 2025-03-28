# import socket
import unittest

from src.client import handle_message
from unittest.mock import MagicMock, patch


class TestClient(unittest.TestCase):

    @patch('builtins.input', side_effect=["hello", "DESCONEXION"])
    def test_client_receive_response(self, mock_input):
        "Test case: Any message sent to the server is received back in caps."
        mock_socket = MagicMock()

        mock_socket.recv.return_value = b"HELLO"

        with patch("socket.socket", return_value=mock_socket):
            handle_message(mock_socket)

        mock_socket.sendall.assert_any_call(b"hello")
        mock_socket.recv.assert_called()

    @patch('builtins.input', side_effect=["DESCONEXION"])
    def test_client_disconnect(self, mock_input):
        "Test case: Terminate session upon client sending 'DESCONEXION' input."
        mock_socket = MagicMock()

        mock_socket.recv.return_value = b""

        with patch("socket.socket", return_value=mock_socket):
            handle_message(mock_socket)

        mock_socket.sendall.assert_called_with(b"DESCONEXION")
        mock_socket.close.assert_called()
