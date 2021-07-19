from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path_csv, type_report):
        with open(path_csv, mode="r") as file:
            content = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = [
              row
              for row in content
            ]
            print(list_products[0])

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
            return report
        else:
            report = CompleteReport.generate(list_products)
            return report
        


if __name__ == "__main__":
    inventory = Inventory()
    # inventory.import_data("../data/inventory.csv")