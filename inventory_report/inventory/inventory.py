from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict
from csv import DictReader
from json import load


class Inventory:

    def load_by_extension(path, content):
        if path.endswith('.csv'):
            return list(DictReader(content))
        elif path.endswith('.json'):
            return load(content)
        elif path.endswith('.xml'):
            xml_orderedDict = xmltodict.parse(content.read())
            records = xml_orderedDict['dataset']['record']
            return [
                dict(product)
                for product
                in records
            ]

    def import_data(path, report_type):
        with open(path, mode='r') as content:
            content_dict = Inventory.load_by_extension(path, content)

            if report_type == 'simples':
                return SimpleReport.generate(content_dict)
            elif report_type == 'completo':
                return CompleteReport.generate(content_dict)
            return None
