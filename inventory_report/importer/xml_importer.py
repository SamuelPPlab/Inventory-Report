from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if "xml" not in file_path:
            raise ValueError("Arquivo inválido")
        return Inventory.handling_xml(file_path)
