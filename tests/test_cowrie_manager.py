import unittest
from unittest.mock import patch, MagicMock
from controller import cowrie_manager 

class TestCowrieManager(unittest.TestCase):

    @patch('controller.cowrie_manager.docker.from_env')
    def test_start_cowrie(self, mock_docker):
        mock_client = MagicMock()
        mock_container = MagicMock()
        mock_client.containers.run.return_value = mock_container
        mock_docker.return_value = mock_client

        container = cowrie_manager.start()
        self.assertEqual(container, mock_container)
        mock_client.containers.run.assert_called_once()

if __name__ == "__main__":
    unittest.main()
