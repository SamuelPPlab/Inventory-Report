from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    def import_data(file_name):
        if file_name.endswith('.json'):
            file_json = Inventory.read_file_json(file_name)
            return file_json

        raise ValueError("Arquivo inválido")
