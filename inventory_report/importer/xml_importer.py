from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            inventory_data = xmltodict.parse(file.read())
            list_inventory = [
                dict(data) for data in inventory_data["dataset"]["record"]
            ]
            return list_inventory
