from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(data):
        if data.endswith(".xml"):
            return Inventory.xml_file(data)
        else:
            raise ValueError("Arquivo inválido")
