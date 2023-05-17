import requests

class PokemonAPI:
    def __init__(self):
        self.base_url = 'https://pokeapi.co/api/v2/'

    def get_pokemon_info(self, number):
        url = self.base_url + f'pokemon/{number}'
        response = requests.get(url)
        
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_number = pokemon_data['id']
            pokemon_types = [type_data['type']['name'] for type_data in pokemon_data['types']]
            return pokemon_number, pokemon_types
        if response.status_code == 404 or response.status_code == 500:
            return None