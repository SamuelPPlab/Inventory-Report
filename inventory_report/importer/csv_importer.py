from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".csv"):
            return Inventory.csv_report(file_name)
        raise ValueError("Arquivo inválido")
