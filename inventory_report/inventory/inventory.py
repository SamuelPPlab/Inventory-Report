from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    def verify(opt, data):
        if opt == "simples":
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)

    def csv_convert(file, opt):
        csv_to_dict = csv.DictReader(file)
        converted_dict = list(csv_to_dict)
        return Inventory.verify(opt, converted_dict)

    def json_convert(file, opt):
        json_to_dict = json.load(file)
        return Inventory.verify(opt, json_to_dict)

    def import_data(str, opt):
        file = open(str)

        if str.endswith('.csv'):
            return Inventory.csv_convert(file, opt)
        if str.endswith('.json'):
            return Inventory.json_convert(file, opt)
