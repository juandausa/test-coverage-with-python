import unittest
import responses
from unittest.mock import patch
from .pokemon_api import PokemonAPI


'''
import responses
import requests

@responses.activate
def test_simple():
    responses.add(responses.GET, 'http://twitter.com/api/1/foobar',
                  json={'error': 'not found'}, status=404)

    resp = requests.get('http://twitter.com/api/1/foobar')

    assert resp.json() == {"error": "not found"}

    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == 'http://twitter.com/api/1/foobar'
    assert responses.calls[0].response.text == '{"error": "not found"}'
'''

class PokemonAPITest(unittest.TestCase):
    def setUp(self):
        self.api = PokemonAPI()

    def test_get_pokemon_info_valid(self):
        responses.add(responses.GET, 'https://pokeapi.co/api/v2/pokemon/25', 
                    json={
                        'id': 25,
                        'types': [
                            {'type': {'name': 'electric'}},
                        ]
                    },
                    status=200)
        
        pokemon_info = self.api.get_pokemon_info(25)

        self.assertEqual(pokemon_info, (25, ['electric']))

    def test_get_pokemon_info_invalid(self):
        pokemon_info = self.api.get_pokemon_info(2000)

        self.assertIsNone(pokemon_info)
