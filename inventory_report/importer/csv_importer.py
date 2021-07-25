from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_path):
        if file_path.endswith("csv"):
            with open(file_path, 'r') as csv_file:
                content = csv.DictReader(csv_file)
                converted_content = list(content)
                return converted_content
        else:
            raise ValueError("Arquivo inválido")
