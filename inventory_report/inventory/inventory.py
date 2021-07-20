from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def import_data(cls, file_path):
        report_simple = SimpleReport.generate(file_path)


# with open("./inventory_report/data/inventory.csv") as file:
#     beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
#     header, *data = beach_status_reader

# print(data)
