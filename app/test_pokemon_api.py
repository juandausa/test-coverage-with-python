import unittest
import responses
from .pokemon_api import PokemonAPI


class PokemonAPITest(unittest.TestCase):
    def setUp(self):
        self.api = PokemonAPI()

    def test_get_pokemon_info_valid(self):
        responses.add(
            responses.GET,
            "https://pokeapi.co/api/v2/pokemon/25",
            json={
                "id": 25,
                "types": [
                    {"type": {"name": "electric"}},
                ],
            },
            status=200,
        )

        pokemon_info = self.api.get_pokemon_info(25)

        self.assertEqual(pokemon_info, (25, ["electric"]))

    def test_get_pokemon_info_invalid(self):
        pokemon_info = self.api.get_pokemon_info(2000)

        self.assertIsNone(pokemon_info)
