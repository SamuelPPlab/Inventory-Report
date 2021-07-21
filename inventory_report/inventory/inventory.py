import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def import_data(report_path, report_type):
        document_type = report_path[-3:]
        report_list = []
        if document_type == "csv":
            with open(report_path, mode="r") as file:
                report_reader = csv.DictReader(file)
                for row in report_reader:
                    report_list.append(row)

        elif document_type == "son":
            with open(report_path, mode="r") as file:
                report_reader = file.read()
                report_list = json.loads(report_reader)

        if report_type == "simples":
            return SimpleReport.generate(report_list)
        else:
            return CompleteReport.generate(report_list)
