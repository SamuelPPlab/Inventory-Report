from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def import_data(path, report):
        list_data = []
        if path[-3::] == "csv":
            list_data = Inventory.csv_report(path)
        elif path[-4::] == "json":
            list_data = Inventory.json_report(path)
        elif path[-3::] == "xml":
            list_data = Inventory.xml_report(path)
        return Inventory.choose_report(report, list_data)

    def csv_report(path):
        with open(path) as file:
            beach_status_reader = csv.reader(
                file, delimiter=",", quotechar='"'
            )
            headers, *data = beach_status_reader
            list_data = []
            value = {}
            for e in data:
                for i in headers:
                    value[i] = e[headers.index(i)]
                    if i == headers[-1]:
                        list_data.append(value)
                        value = {}
        return list_data

    def json_report(path):
        with open(path) as file:
            content = file.read()
            list_data = json.loads(content)
            return list_data

    def xml_report(path):
        list_data = []
        with open(path) as file:
            doc = xmltodict.parse(file.read())
            doc = doc["dataset"]["record"]
            for i in doc:
                obj = {}
                for key, value in i.items():
                    obj[key] = value
                list_data.append(obj)
        return list_data

    def choose_report(report, list_data):
        if report == "simples":
            return SimpleReport.generate(list_data)
        elif report == "completo":
            return CompleteReport.generate(list_data)


# print(Inventory.import_data
# ("inventory_report/data/inventory.xml", "simples"))
