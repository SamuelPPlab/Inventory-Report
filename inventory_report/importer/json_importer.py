from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".json"):
            return Inventory.json_report(file_name)
        raise ValueError("Arquivo inválido")
