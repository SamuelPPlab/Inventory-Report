import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def xml_helper(cls, content):
        content_dict = xmltodict.parse(content.read())
        return [dict(item) for item in content_dict["dataset"]["record"]]

    @classmethod
    def load(cls, path):
        with open(path, mode="r") as content:
            if path.endswith(".json"):
                return json.load(content)
            elif path.endswith(".xml"):
                return cls.xml_helper(content)
            elif path.endswith(".csv"):
                return list(csv.DictReader(content))
            else:
                return None

    @classmethod
    def import_data(cls, path, type):
        list = cls.load(path)
        if type == "completo":
            return CompleteReport.generate(list)
        elif type == "simples":
            return SimpleReport.generate(list)
        return None
