from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')
        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            list_data = []
            for item in root:
                object_format = {}
                for attr in item:
                    object_format[attr.tag] = attr.text
                list_data.append(object_format)
        return list_data

# referencia:
# https://www.geeksforgeeks.org/reading-and-writing-xml-files-in-python/
