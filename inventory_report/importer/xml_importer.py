from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(file_path):
        if (file_path[len(file_path) - 4:] != '.xml'):
            raise ValueError('Arquivo inválido')
        with open(file_path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            iterable_data = []
            for child in root:
                iterable_data.append({tag.tag: tag.text for tag in child})
            return iterable_data
