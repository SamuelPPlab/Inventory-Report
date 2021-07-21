from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(file_name):
        if file_name.endswith(".xml"):
            return Inventory.xml_report(file_name)
        raise ValueError("Arquivo inválido")
