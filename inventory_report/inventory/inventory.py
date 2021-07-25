import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


# class Inventory:
#     @classmethod
#     def xml_helper(cls, content):
#         content_dict = xmltodict.parse(content.read())
#         return [dict(item) for item in content_dict["dataset"]["record"]]

#     @classmethod
#     def load(cls, path):
#         with open(path, mode="r") as content:
#             if path.endswith(".json"):
#                 return json.load(content)
#             elif path.endswith(".xml"):
#                 return cls.xml_helper(content)
#             elif path.endswith(".csv"):
#                 return list(csv.DictReader(content))
#             else:
#                 return None

#     @classmethod
#     def import_data(cls, path, type):
#         list = cls.load(path)
#         if type == "completo":
#             return CompleteReport.generate(list)
#         elif type == "simples":
#             return SimpleReport.generate(list)
#         return None
class Inventory:
    @classmethod
    def read_csv_file(cls, csv_content):
        return list(csv.DictReader(csv_content))

    @classmethod
    def read_json_file(cls, json_content):
        return json.load(json_content)

    @classmethod
    def read_xml_file(cls, xml_content):
        xml_content_dict = xmltodict.parse(xml_content.read())
        return [
            dict(product) for product in xml_content_dict["dataset"]["record"]
        ]

    @classmethod
    def load_file(cls, path):
        with open(path, mode="r") as content:
            if path.endswith(".csv"):
                return cls.read_csv_file(content)
            elif path.endswith(".json"):
                return cls.read_json_file(content)
            elif path.endswith(".xml"):
                return cls.read_xml_file(content)
            else:
                return None

    @classmethod
    def import_data(cls, path, type):
        product_list = cls.load_file(path)
        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)

        return None
