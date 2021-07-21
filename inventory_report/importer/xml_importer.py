from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file) as file_xml:
            inventory = xmltodict.parse(file_xml.read())
            result = inventory["dataset"]["record"]
        return result
