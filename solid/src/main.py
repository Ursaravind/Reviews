from src.api_services.pokemon_api import PokemonApi
from data_exporters.csv_data_exporter import CsvExporter
from data_exporters.text_data_exporter import TextExporter
from src.data_exporters.pdf_data_exporter import PdfExport


class Main:
    @staticmethod
    def csv_exporter():
        csv_exporter = CsvExporter(PokemonApi=PokemonApi)
        csv_exporter.data_exporter()

    @staticmethod
    def text_exporter(csv_url):
        text_exporter = TextExporter()
        text_exporter.data_exporter(csv_url=csv_url)

    @staticmethod
    def pdf_exporter(text_url,pdf_url):
        pdf_exporter = PdfExport()
        pdf_exporter.data_exporter(text_url=text_url,pdf_file_path=pdf_url)

    @staticmethod
    def show_menu():
        while True:
            print("*" * 30)
            print("Choose an option to get Pokémon data:")
            print("1. Export CSV")
            print("2. Export Text from CSV")
            print("3. Export PDF from Text")
            print("0. Exit")
            print("*" * 30)

            try:
                user_input = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 3.")
                continue

            if user_input == 0:
                print("Exiting program.")
                break
            elif user_input == 1:
                Main.csv_exporter()
            elif user_input == 2:
                csv_url = "processed_data/pokemon_abilities.csv"
                Main.text_exporter(csv_url)
            elif user_input == 3:
                text_url = "processed_data/pokemon_abilities.txt"
                pdf_url = "processed_data/pokemon_abilities.pdf"
                Main.pdf_exporter(text_url,pdf_url)
            else:
                print("Invalid choice. Please select between 0 and 3.")

    @staticmethod
    def run():
        Main.show_menu()



if __name__ == "__main__":
    Main.run()
