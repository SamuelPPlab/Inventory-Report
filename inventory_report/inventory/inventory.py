import json
import csv
import xmltodict
from inventory_report.reports import (
    complete_report,
    simple_report,
)

SimpleReport = simple_report.SimpleReport
CompleteReport = complete_report.CompleteReport


class Inventory(CompleteReport):
    def __init__(self) -> None:
        self.sr = SimpleReport()
        self.cr = CompleteReport()

    @classmethod
    def import_data(cls, path: str, mode: str) -> str:
        content = []
        if path.endswith(".json"):
            content = cls().import_json(path)
        elif path.endswith(".csv"):
            content = cls().import_csv(path)
        elif path.endswith(".xml"):
            content = cls().import_xml(path)

        return cls().execute(content, mode)

    def execute(self, data: list, mode: str) -> str:
        return (
            self.sr.generate(data)
            if mode == "simples"
            else self.cr.generate(data)
        )

    @staticmethod
    def import_json(path: str) -> list:
        with open(path, "r") as f:
            return list(json.loads(f.read()))

    @staticmethod
    def import_csv(path: str) -> list:
        with open(path, "r") as f:
            return list(csv.DictReader(f))

    @staticmethod
    def import_xml(path: str) -> list:
        with open(path, "r") as f:
            content = f.read()

        return list(xmltodict.parse(content)["dataset"]["record"])
