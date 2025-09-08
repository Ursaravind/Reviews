from interfaces.api_interface import Api
import requests


class PokemonApi(Api):
    """A class to handle API requests for fetching Pokémon data.

    This class implements the Api interface and provides methods to retrieve
    Pokémon information from the Pokémon API.
    """

    @staticmethod
    def get_data(url):
        """Fetch Pokémon data from the given URL.

        Args:
            url (str): The URL to fetch Pokémon data from the Pokémon API.

        Returns:
            list: A list of dictionaries containing Pokémon details (name, height,
                  weight, and abilities).

        Raises:
            requests.exceptions.RequestException: If the API request fails.
        """
        response = requests.get(url)
        result = []
        if response.status_code == 200:
            data = response.json()
            pokemons = data["results"]
            for pokemon in pokemons:
                poke_response = requests.get(pokemon["url"])
                if poke_response.status_code == 200:
                    poke_data = poke_response.json()
                    name = poke_data.get("name")
                    height = poke_data.get("height")
                    weight = poke_data.get("weight")
                    abilities = [
                        a["ability"]["name"] for a in poke_data.get("abilities", [])
                    ]
                    result.append(
                        {
                            "name": name,
                            "height": height,
                            "weight": weight,
                            "abilities": ", ".join(abilities),
                        }
                    )
            return result