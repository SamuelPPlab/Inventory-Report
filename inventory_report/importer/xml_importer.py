from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith('.xml'):
            with open(path) as file:
                content = file.read()
                return list(xmltodict.parse(content)["dataset"]["record"])
        else:
            raise ValueError("Arquivo inválido")
