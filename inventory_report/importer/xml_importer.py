import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if not (file_path.endswith(".xml")):
            raise ValueError("Arquivo inválido")
        with open(file_path) as fd:
            file = xmltodict.parse(fd.read())
            products = file["dataset"]["record"]
            dict_products = [
                {
                    item: product[item]
                    for item in product
                }
                for product in products
            ]
        return dict_products
