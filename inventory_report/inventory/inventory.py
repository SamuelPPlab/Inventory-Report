from inventory_report.reports.complete_report import (
    SimpleReport,
    CompleteReport,
)
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def read_csv(path):
        with open(path, "r") as file:
            return [row for row in csv.DictReader(file)]

    @staticmethod
    def read_json(path):
        with open(path, "r") as file:
            return json.loads(file.read())

    @staticmethod
    def read_xml(path):
        stock = []
        for node in ET.parse(path).getroot():
            company = {}
            for record in node:
                company[record.tag] = record.text
            stock.append(company)
        return stock

    @staticmethod
    def import_data(path, report_type):
        file_type = path[-3:]
        if file_type == "csv":
            file = Inventory.read_csv(path)
        elif file_type == "xml":
            file = Inventory.read_xml(path)
        else:
            file = Inventory.read_json(path)
        if report_type == "simples":
            return SimpleReport.generate(file)
        else:
            return CompleteReport.generate(file)
