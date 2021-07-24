from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict
import json
import csv


class Inventory:
    def import_data(path, report_type):
        if path.split(".")[1] == "csv":
            with open(path, mode="r") as file:
                file_reader = csv.DictReader(file)
                list = []
                for string in file_reader:
                    list.append(string)
            return Generate_Report.generate(list, report_type)

        if path.split(".")[1] == "json":
            with open(path, mode="r") as file:
                list = json.load(file)
            return Generate_Report.generate(list, report_type)

        if path.split(".")[1] == "xml":
            with open(path, mode="r") as file:
                xml_file = file.read()
                list = json.dumps(xmltodict.parse(xml_file))
                result = json.loads(list)  # loads @vanderson-henrique
                final_list = result["dataset"]["record"]
            return Generate_Report.generate(final_list, report_type)


class Generate_Report:
    def generate(list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(list)
        return CompleteReport.generate(list)
