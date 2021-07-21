import csv
from inventory_report.importer.importer import FileExtension, Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name: str):
        file_extension: str = Importer.get_file_extension(file_name)

        if file_extension != FileExtension.CSV.value:
            raise ValueError("Arquivo inválido")

        with open(file_name, "r") as file:
            return [line for line in csv.DictReader(file)]
