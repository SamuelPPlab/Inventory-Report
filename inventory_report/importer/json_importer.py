from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, data):
        if not data.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return Inventory.json_open(data)
