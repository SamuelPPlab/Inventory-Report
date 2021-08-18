import xml.etree.cElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" in path:
            etRoot = ET.parse(path).getroot()

            data = [
                {item.tag: item.text for item in record} for record in etRoot
            ]

            return data
        else:
            raise ValueError("Arquivo inválido")
