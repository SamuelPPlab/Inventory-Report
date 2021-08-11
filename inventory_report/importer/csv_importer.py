from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith(".csv"):
            return Inventory.csv_file(data)
        else:
            raise ValueError("Arquivo inválido")
