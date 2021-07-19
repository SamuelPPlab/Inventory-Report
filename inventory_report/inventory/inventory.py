import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, mode):
        if path.endswith(".csv"):
            content = cls.read_csv(path)
        if path.endswith(".json"):
            content = cls.read_json(path)
        if path.endswith(".xml"):
            content = cls.read_xml(path)
        if mode == "simples":
            content = SimpleReport.generate(content)
        else:
            content = CompleteReport.generate(content)
        return content

    @classmethod
    def read_csv(cls, path):
        with open(path) as file:
            return list(csv.DictReader(file))

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            return (json.load(file))

    @classmethod
    def read_xml(cls, path):
        with open(path) as file:
            content = file.read()
            return list(xmltodict.parse(content)["dataset"]["record"])
