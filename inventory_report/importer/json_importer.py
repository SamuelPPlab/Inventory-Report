from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(path):
        file_type = path[-4:]
        if file_type != "json":
            raise ValueError("Arquivo inválido")
        return Inventory.read_json(path)
