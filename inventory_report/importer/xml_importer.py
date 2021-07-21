# import xml
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file):
        if file.endswith(".xml"):
            # with open(file, mode="r") as xml_content:
            #     xml_content_dict = xml.parse(xml_content.read())
            #     return [
            #         dict(product)
            #         for product in xml_content_dict["dataset"]["record"]
            #     ]
            tree = ET.parse(file)
            root = tree.getroot()
            records = list(root)
            elements = [list(record) for record in records]
            dict_from_xml = [
                {item.tag: item.text for item in element}
                for element in elements
            ]
            return dict_from_xml

        raise ValueError("Arquivo inválido")
