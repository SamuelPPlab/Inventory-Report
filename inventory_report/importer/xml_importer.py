import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(file_path: str) -> list:
        if file_path.endswith(".xml"):
            with open(file_path, mode="r") as file:
                content = xmltodict.parse(file.read())
                return [
                    dict(product)
                    for product in content["dataset"]["record"]
                ]

        raise ValueError("Arquivo inválido")
