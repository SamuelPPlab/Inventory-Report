from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    """Comentario para subir pr Raphael Caputo"""

    @classmethod
    def import_data(cls, xml_data):
        if not xml_data.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return Inventory.open_xml_archive(xml_data)
