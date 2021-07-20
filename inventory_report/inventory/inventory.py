from csv import DictReader
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xmltodict
from json import load


class Inventory:
    def load_by_extension(path, content):
        if path.endswith('.csv'):
            return list(DictReader(content))
        elif path.endswith('.json'):
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
        with open(path, mode='r') as content:
            content_dict = Inventory.load_by_extension(path, content)
            if report_type == 'simples':
                return SimpleReport.generate(content_dict)
            else:
                report_type == 'completo'
                return CompleteReport.generate(content_dict)
            return None
