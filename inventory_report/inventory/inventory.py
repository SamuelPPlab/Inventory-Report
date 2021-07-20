from csv import DictReader
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self, receive_file, report_type):
        self.file = receive_file
        self.report_type = report_type

    def import_data(receive_file, report_type):
        data = []
        with open(receive_file, 'r') as file:
            if file.name[-1] == 'n':
                data = json.load(file)
            csvReader = DictReader(file)
            for rows in csvReader:
                data.append(rows)

        if report_type == 'simples':
            return SimpleReport.generate(data)
        elif report_type == 'completo':
            return CompleteReport.generate(data)
