import requests

"""Testing api """

def get_pokemon_details():
    """This method tests the api and check the results"""
    
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemons = data["results"]
        for pokemon in pokemons:
            poke_response = requests.get(pokemon["url"])
            if poke_response.status_code == 200:
                poke_data = poke_response.json()
                name = poke_data["name"]
                height = poke_data["height"]
                weight = poke_data["weight"]
                abilities = [a["ability"]["name"] for a in poke_data["abilities"]]
                print(f"Name: {name}, Height: {height}, Weight: {weight}, Abilities: {abilities}")
            else:
                print(f"Failed to fetch details for {pokemon['name']}")
    else:
        print("Failed to fetch Pokémon list.")

get_pokemon_details()