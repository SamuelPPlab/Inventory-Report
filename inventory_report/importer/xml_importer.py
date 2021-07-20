from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if (path.endswith('.xml')):
            tree = ET.parse(path)
            root = tree.getroot()
            result = []
            for record in root.findall("record"):
                dictionary = {}
                for tag in record:
                    dictionary[tag.tag] = tag.text
                result.append(dictionary)
            return result
        else:
            raise ValueError('Arquivo inválido')
