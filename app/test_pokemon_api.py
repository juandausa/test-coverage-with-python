import unittest
from unittest.mock import patch
from .pokemon_api import PokemonAPI

class PokemonAPITest(unittest.TestCase):
    def setUp(self):
        self.api = PokemonAPI()

    @patch('pokemon_api.requests.get')
    def test_get_pokemon_info_valid(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'id': 25,
            'types': [
                {'type': {'name': 'electric'}},
            ]
        }

        pokemon_info = self.api.get_pokemon_info(25)

        self.assertEqual(pokemon_info, (25, ['electric']))
        mock_get.assert_called_once()

    @patch('pokemon_api.requests.get')
    def test_get_pokemon_info_invalid(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        pokemon_info = self.api.get_pokemon_info(1000)

        self.assertIsNone(pokemon_info)
        mock_get.assert_called_once()