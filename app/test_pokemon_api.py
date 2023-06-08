import unittest
import responses
from .pokemon_api import PokemonAPI

class PokemonAPITest(unittest.TestCase):
    def setUp(self):
        self.api = PokemonAPI()

    @responses.activate
    def test_get_pokemon_info_valid(self):
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/25'
        responses.add(responses.GET, pokemon_url, 
                    json={
                        'id': 25,
                        'types': [
                            {'type': {'name': 'electric'}},
                        ]
                    },
                    status=200)
        
        pokemon_info = self.api.get_pokemon_info(25)

        self.assertEqual(pokemon_info, (25, ['electric']))
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, pokemon_url)

    def test_get_pokemon_info_not_found(self):
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/2000'
        responses.add(responses.GET, pokemon_url, 
                    json={
                        'error': 'Pokemon not found'
                    },
                    status=404)
        
        pokemon_info = self.api.get_pokemon_info(2000)

        self.assertIsNone(pokemon_info)

#   @responses.activate
#   def test_get_pokemon_info_not_available(self):
