import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def handling_csv(csv_path):
        with open(csv_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            list_data = list(reader)

        return list_data

    def handling_json(json_path):
        with open(json_path, "r") as json_file:
            list_data = json.load(json_file)

        return list_data

    def handling_xml(xml_path):
        with open(xml_path, "r") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            list_data = []
            for child in root:
                list_data.append({tag.tag: tag.text for tag in child})

        return list_data

    @classmethod
    def checkTypeFile(cls, file_path):
        if "csv" in file_path:
            return cls.handling_csv(file_path)
        elif "json" in file_path:
            return cls.handling_json(file_path)
        else:
            return cls.handling_xml(file_path)

    @classmethod
    def import_data(cls, file_path, report_type):
        data = cls.checkTypeFile(file_path)
        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
