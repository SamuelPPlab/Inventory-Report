import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


class Inventory:
    def read_csv(report_path):
        report_list = []
        with open(report_path, mode="r") as file:
            report_reader = csv.DictReader(file)
            for row in report_reader:
                report_list.append(row)
        return report_list

    def read_json(report_path):
        with open(report_path, mode="r") as file:
            report_reader = file.read()
            return json.loads(report_reader)

    def read_xml(report_path):
        report_list = []
        tree = ET.parse(report_path)
        root = tree.getroot()
        all_records = root.findall('record')
        for record in all_records:
            element = {}
            for item in record:
                element[item.tag] = item.text
            report_list.append(element)
        return report_list

    def import_data(report_path, report_type):
        document_type = report_path[-3:]

        if document_type == "csv":
            report_list = Inventory.read_csv(report_path)

        elif document_type == "son":
            report_list = Inventory.read_json(report_path)

        elif document_type == "xml":
            report_list = Inventory.read_xml(report_path)

        else:
            raise ValueError("Arquivo inválido")

        if report_type == "simples":
            return SimpleReport.generate(report_list)
        else:
            return CompleteReport.generate(report_list)
