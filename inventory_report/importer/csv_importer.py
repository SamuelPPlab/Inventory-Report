from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")
        with open(path, mode="r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = [row for row in content]
            print("CSV", list_products[0])
            return list_products


if __name__ == "__main__":
    # csv_importer = CsvImporter()
    CsvImporter.import_data("inventory_report/data/inventory.csv")
