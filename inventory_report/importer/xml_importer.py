import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def read_xml(path):
        tree = ET.parse(path)
        root = tree.getroot()
        records = list(root)

        data = []
        for record in records:
            new_product = {}
            product = list(record)

            for key in product:
                new_product[key.tag] = key.text
            data.append(new_product)

        return data

    @staticmethod
    def import_data(path):
        file_format = path.split(".")[-1]

        if file_format != "xml":
            raise ValueError("Arquivo inválido")

        return XmlImporter.read_xml(path)
