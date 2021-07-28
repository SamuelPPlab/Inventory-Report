from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if "csv" not in file_path:
            raise ValueError("Arquivo inválido")
        return Inventory.handling_csv(file_path)
