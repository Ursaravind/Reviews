import csv
from interfaces.data_exporter_interface import DataParser
from api_urls.get_api_urls import pokemon_url


class CsvExporter(DataParser):
    """A class to export Pokémon data to a CSV file.

    This class implements the DataParser interface and handles the export of
    Pokémon data retrieved from the PokemonApi to a CSV file.
    """

    def __init__(self, PokemonApi):
        """Initialize the CsvExporter with a PokemonApi instance.

        Args:
            PokemonApi: An instance of the PokemonApi class to fetch data.
        """
        self.poki_object = PokemonApi

    def data_exporter(self, filename):
        """Export Pokémon data to a CSV file.

        Args:
            filename (str, optional): The path to the output CSV file.
                Defaults to "processed_data/pokemon_abilities.csv".

        Notes:
            Prints status messages indicating success or failure of the export.
        """
        data = self.poki_object.get_data(pokemon_url)
        if not data:
            print("No data to export.")
            return

        keys = data[0].keys()
        print(keys)
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully exported to {filename}.")