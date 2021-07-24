from inventory_report.importer.importer import Importer
import xmldict
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(open(path))
        root = tree.getroot()
        return xmldict.xml_to_dict(root)["dataset"]["record"]