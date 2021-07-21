from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as file:
            list_products = json.load(file)
            # print("JSON", list_products[0])
            return list_products


if __name__ == "__main__":
    importer = JsonImporter()
    importer.import_data("inventory_report/data/inventory.json")
    # JsonImporter.import_data("inventory_report/data/inventory.json")
