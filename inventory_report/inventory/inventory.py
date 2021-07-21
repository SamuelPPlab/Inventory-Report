import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(report_path, report_type):
        with open(report_path, mode="r") as file:
            report_reader = csv.DictReader(file)
            report_list = []
            for row in report_reader:
                report_list.append(row)
            print(report_list)
        if report_type == "simples":
            return SimpleReport.generate(report_list)
        else:
            return CompleteReport.generate(report_list)
