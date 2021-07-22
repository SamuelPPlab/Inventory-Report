from inventory_report.importer.importer import Importer
import xml.etree.cElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        extension = path.split(".")
        value = extension[len(extension) - 1]
        if value == "xml":
            xml = ET.parse(path)
            xml_root = xml.getroot()
            data = [
                {item.tag: item.text for item in record} for record in xml_root
            ]
            return data
        else:
            raise ValueError("Arquivo inválido")


if __name__ == "__main__":
    csv1 = XmlImporter()
    csv1.import_data("./inventory_report/data/inventory.xml")
