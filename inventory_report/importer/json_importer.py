from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if "json" not in file_path:
            raise ValueError("Arquivo inválido")
        return Inventory.handling_json(file_path)
