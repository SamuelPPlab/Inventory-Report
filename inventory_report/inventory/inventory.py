import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, csv):
        pass

    def import_data(path, type):
        with open(path, "r") as file:
            ending = path[-3:]
            if ending == 'csv':
                result = [row for row in csv.DictReader(file)]
                if type == "simples":
                    return SimpleReport.generate(result)
                return CompleteReport.generate(result)
            if ending == 'son':
                print('json')
            if ending == 'xml':
                print('xml')
