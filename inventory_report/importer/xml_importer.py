import xml
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file):
        if file.endswith(".xml"):
            with open(file, mode="r") as xml_content:
                xml_content_dict = xml.parse(xml_content.read())
                return [
                    dict(product)
                    for product in xml_content_dict["dataset"]["record"]
                ]

        raise ValueError("Arquivo inválido")
