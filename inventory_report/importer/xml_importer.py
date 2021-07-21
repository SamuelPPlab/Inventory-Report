from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        root = tree.getroot()
        list_products = [
            {
                tag.tag: tag.text
                for tag in child
            }
            for child in root
        ]
        print("XML", list_products[0])
        return list_products


if __name__ == "__main__":
    XmlImporter.import_data("inventory_report/data/inventory.xml")
