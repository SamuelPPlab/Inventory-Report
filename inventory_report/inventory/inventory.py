from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
from xml_to_dict import XMLtoDict


class Inventory:
    def read_csv_file(path):
        with open(path, 'r') as csv_file:
            csv_list = csv.DictReader(csv_file)
            return [product for product in csv_list]

    def read_json_file(path):
        with open(path, 'r') as json_file:
            json_list = json.load(json_file)
            return json_list

    def read_xml_file(path):
        with open(path, 'r') as xml_file:
            parser = XMLtoDict()
            xml_list = xml_file.read()
            print(parser.value_from_nest("record", xml_list))
            return parser.value_from_nest("record", xml_list)

    def verify_file_format(cls, path):
        if path.endswith("csv"):
            return cls.read_csv_file(path)
        elif path.endswith("json"):
            return cls.read_json_file(path)
        else:
            return cls.read_xml_file(path)

    @classmethod
    def import_data(cls, path, type):
        formated_list = cls.verify_file_format(cls, path)
        if type == "simples":
            return SimpleReport.generate(formated_list)
        else:
            return CompleteReport.generate(formated_list)


# Andre Horman e Lucca Focosi - Carol Andrade e Strongreen
# https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes
# https://www.programmersought.com/article/99101354414/
# https://app.betrybe.com/course/computer-science/introducao-a-python-e-raspagem-de-dados-da-web/entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/61a9ebdb-e772-49d0-a97f-06c8694d657e/manipulando-arquivos-csv/63829da9-e433-4037-95dc-d401d0dd89b0?use_case=side_bar
