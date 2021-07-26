from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if path.endswith('.xml'):
            with open(path, mode='r') as file:
                inventory = xmltodict.parse(file.read())
                return inventory["dataset"]["record"]

        raise ValueError("Arquivo inválido")
