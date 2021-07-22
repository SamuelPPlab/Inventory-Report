from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        ending = file_name[-3:]
        if ending == 'son':
            json = Inventory.import_json(file_name)
            return json
        else:
            raise ValueError("Arquivo inválido")
