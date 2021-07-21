from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def import_data(str, opt):
        with open(str, 'r') as file:
            if str.endswith('.csv'):
                csv_to_dict = csv.DictReader(file)
                converted_dict = list(csv_to_dict)
                return Inventory.verify(opt, converted_dict)

    def verify(opt, data):
        if opt == "simples":
            return SimpleReport.generate(data)

        return CompleteReport.generate(data)
