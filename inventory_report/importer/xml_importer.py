from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(file):
        if file.endswith("xml"):
            with open(file) as file:
                reader = xmltodict.parse(file.read())
                return reader["dataset"]["record"]

        else:
            raise ValueError("Arquivo inválido")
