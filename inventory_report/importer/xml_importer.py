import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path_document):
        if not (path_document.endswith(".xml")):
            raise ValueError("Arquivo inválido")
        with open(path_document) as f:
            doc = xmltodict.parse(f.read())
            all_product = doc["dataset"]["record"]
            file_in_dict = [
                {
                    item: product[item]
                    for item in product
                }
                for product in all_product
            ]

        return file_in_dict
