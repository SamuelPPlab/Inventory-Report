from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(file):
        if file.endswith(".json"):
            with open(file, mode="r") as content:
                return Inventory.load_by_extension(file, content)

        raise ValueError("Arquivo inválido")
