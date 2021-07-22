import csv
import json
from lxml import etree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_name, report_type):
        file_extension = file_name[-4:]
        reports_list = []

        if (file_extension == '.csv'):
            with open(file_name) as file:
                content = csv.DictReader(file)
                reports_list = list(map(lambda x: x, content))
        elif (file_extension == '.xml'):
            with open(file_name) as file:
                tree = etree.parse(file)
                root = tree.getroot()
                for item in root:
                    d = {}
                    for elem in item:
                        d[elem.tag] = elem.text
                    reports_list.append(d)
        else:
            with open(file_name) as file:
                reports_list = json.load(file)

        return cls.generate_report(report_type, reports_list)

    def generate_report(report_type, reports_list):
        if (report_type == 'simples'):
            return SimpleReport.generate(reports_list)
        else:
            return CompleteReport.generate(reports_list)