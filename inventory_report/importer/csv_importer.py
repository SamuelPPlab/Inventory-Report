from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, data):
        if not data.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return Inventory.open_csv_archive(data)
