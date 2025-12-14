from fpdf import FPDF
import csv


class PdfExport:
    """A class to export data from a CSV file to a PDF document.

    This class handles the conversion of CSV data into a formatted PDF file.
    """

    def data_exporter(self, csv_file_path,pdf_file_path):
        """Export data from a CSV file to a PDF document.

        Args:
           csv_file_path (str, optional): The path to the input CSV file.

        Notes:
            Creates a PDF with a fixed column width layout and prints status
            messages for success or errors.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        col_widths = [40, 20, 20, 100]
        try:
            with open(csv_file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    for j, datum in enumerate(row):
                        pdf.cell(col_widths[j], 10, datum, border=1)
                    pdf.ln(10)
            pdf.output(pdf_file_path)
            print("PDF exported")
        except FileNotFoundError:
            print("CSV file not found")
        except Exception as e:
            print(f"An error occurred: {e}")