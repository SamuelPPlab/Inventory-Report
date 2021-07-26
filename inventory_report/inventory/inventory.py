from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, file_path, type_report):

        data = []
        extension = file_path.split('.')[1]

        if extension == 'csv':
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)

        elif extension == 'json':
            with open(file_path, "r") as file:
                data = json.load(file)

        else:
            with open(file_path, 'r') as file:
                read = file.read()
                data_xml = xmltodict.parse(read)
                data_json = json.dumps(data_xml)
                result = json.loads(data_json)
                data = result["dataset"]["record"]

        if type_report == 'simples':
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)


# x = Inventory()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.xml",
#     "simples",
# ))

# x = Inventory()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.csv",
#     "completo",
# ))

# x = Inventory()
# print(x.import_data(
#     "/home/vanderson/Trybe/projetos_trybe/BLOCO_36_T6/sd-06-inventory-report/inventory_report/data/inventory.json",
#     "completo",
# ))
