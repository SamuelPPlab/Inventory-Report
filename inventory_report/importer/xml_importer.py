from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path_name):
        if ".xml" in path_name:
            tree = ET.parse(path_name)
            root = tree.getroot()
            xml_result = []

            for item in root.findall('./record'):
                curr_dict = {}

                for child in item:
                    curr_dict[child.tag] = child.text

                xml_result.append(curr_dict)

            return xml_result
        raise ValueError("Arquivo inválido")
