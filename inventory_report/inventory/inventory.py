
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def generate_report(content, report_type):
        if report_type == 'simples':
            return SimpleReport.generate(content)
        return CompleteReport.generate(content)

    def read_CSV_file(file_path, report_type):
        with open(file_path, 'r') as csv_file:
            content = csv.DictReader(csv_file)
            converted_content = list(content)
            return Inventory.generate_report(converted_content, report_type)

    def read_JSON_file(file_path, report_type):
        with open(file_path, 'r') as json_file:
            content = json.load(json_file)
            return Inventory.generate_report(content, report_type)

    def read_xml_file(file_path, report_type):
        with open(file_path, 'r') as xml_file:
            content = xmltodict.parse(xml_file.read())
            converted_content = content["dataset"]["record"]
            return Inventory.generate_report(converted_content, report_type)

    def import_data(file_path, report_type):
        if file_path.endswith('csv'):
            return Inventory.read_CSV_file(file_path, report_type)
        if file_path.endswith('json'):
            return Inventory.read_JSON_file(file_path, report_type)
        if file_path.endswith('xml'):
            return Inventory.read_xml_file(file_path, report_type)
