from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


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
        with open(str) as file:
            if str.endswith('.csv'):
                return Inventory.csv_convert(file, opt)
            elif str.endswith('.json'):
                return Inventory.json_convert(file, opt)
            elif str.endswith('.xml'):
                xml_to_dict = xmltodict.parse(file.read())
                converted_dict = xml_to_dict["dataset"]["record"]
                return Inventory.verify(opt, converted_dict)
        file.close()
