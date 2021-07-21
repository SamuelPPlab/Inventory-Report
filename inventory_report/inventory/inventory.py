import csv
import json
from xml_to_dict import XMLtoDict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def decode(type, data):
    if type == 'csv':
        with open(data, newline="") as csvfile:
            doc_reader = csv.DictReader(csvfile)
            data_csv = list((item for item in doc_reader))
            return data_csv
    elif type == 'xml':
        with open(data) as xml_file:
            teste = xml_file.read()
            parser = XMLtoDict()
            response = parser.value_from_nest('.*ecord', teste)
            return response
    else:
        with open(data) as file:
            result = json.load(file)
            return result


class Inventory():
    def import_data(self, csv_data, report_type):
        type = csv_data[-3:len(csv_data)]
        data = decode(type, csv_data)
        if report_type == 'simples':
            return SimpleReport.generate(data)
        return CompleteReport.generate(data)
