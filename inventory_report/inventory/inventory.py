from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
# import json


class Inventory():
    @classmethod
    def import_data(cls, file_path, report_type='simples'):
        report_list = []
        with open(file_path) as file:
            data = csv.DictReader(file)
            for rows in data:
                report_list.append(rows)

        if (report_type == 'simples'):
            return SimpleReport.generate(report_list)
        elif (report_type == 'completo'):
            return CompleteReport.generate(report_list)
        else:
            return None


print(Inventory.import_data('inventory_report/data/inventory.csv', 'completo'))
