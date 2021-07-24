import xml
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file):
        if file.endswith(".xml"):
            with open(file, mode="r") as xml_content:
                xml_t = xml.parse(xml_content.read())["dataset"]["record"]
                return xml_t
        else:
            raise ValueError("Arquivo inválido")
