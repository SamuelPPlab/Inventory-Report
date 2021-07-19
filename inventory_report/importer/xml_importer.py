from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(path):
        file_type = path[-3:]
        if file_type != "xml":
            raise ValueError("Arquivo inválido")
        return Inventory.read_xml(path)
