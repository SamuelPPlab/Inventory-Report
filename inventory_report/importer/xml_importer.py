from .importer import Importer
from inventory_report.inventory.inventory import Serialize
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if path.split(".")[1] == "xml":
            with open(path, mode="r") as arquivo:
                tree = ET.parse(arquivo)
                data = tree.getroot()
            lista = Serialize.xml_to_list(data)
            return lista
        else:
            raise ValueError("Arquivo inválido")
