from interfaces.data_exporter_interface import DataParser


class TextExporter(DataParser):
    """A class to export data from a CSV file to a text file.

    This class implements the DataParser interface and handles the conversion
    of CSV data into a plain text format.
    """

    def data_exporter(self, csv_url, txt_url):
        """Export data from a CSV file to a text file.

        Args:
            csv_url (str): The path to the input CSV file.
            txt_url (str, optional): The path to the output text file.

        Notes:
            Replaces commas with spaces and joins lines with four spaces.
            Prints a success message upon completion.
        """
        with open(csv_url, "r", encoding="utf-8") as csv_file:
            text = "    ".join([line.strip().replace(",", " ") for line in csv_file])
        with open(txt_url, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        print(f"Text data exported")