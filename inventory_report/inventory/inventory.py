from csv import DictReader
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from json import load
import xmltodict


class Inventory:
    def carregar_extensao(path, content):
        if path.endswith(".csv"):
            return list(DictReader(content))
        elif path.endswith(".json"):
            return load(content)
        else:
            path.endswith(".xml")
            return list(
                map(
                    lambda x: dict(x),
                    xmltodict.parse(content.read())["dataset"]["record"],
                )
            )

    def import_data(path, report_type):
        with open(path, mode="r") as conteudo:
            if report_type == "simples":
                return SimpleReport.generate(
                    Inventory.carregar_extensao(path, conteudo)
                )
            else:
                return CompleteReport.generate(
                    Inventory.carregar_extensao(path, conteudo)
                )
