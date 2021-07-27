from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, xml_data):
        if not xml_data.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return Inventory.xml_open(xml_data)
