import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report):
        if(path.endswith('.csv')):
            file = Inventory.csv_file(path)
        if(path.endswith('.json')):
            file = Inventory.json_file(path)
        if(path.endswith('.xml')):
            file = Inventory.xml_file(path)

        if(report == 'completo'):
            return CompleteReport.generate(file)
        else:
            return SimpleReport.generate(file)

    @staticmethod
    def csv_file(path):
        with open(path) as file:
            data = csv.DictReader(file)
            return list(data)

    @staticmethod
    def json_file(path):
        file = open(path)
        return json.load(file)

    @staticmethod
    def xml_file(path):
        with open(path) as file:
            my_ordered_dict = xmltodict.parse(file.read())["dataset"]["record"]
            return [dict(order) for order in my_ordered_dict]
