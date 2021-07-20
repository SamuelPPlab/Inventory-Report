import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from csv import reader


class Inventory:
    def __init__(self):
        pass

    def import_data(file_path, report_type):
        inv_report = define_importer(file_path)

        if report_type == 'simples':
            return SimpleReport.generate(inv_report)
        elif report_type == 'completo':
            return CompleteReport.generate(inv_report)


def define_importer(file_path):
    inv_report = ""
    file_extension = file_path.split(".")[1]

    if file_extension == 'csv':
        inv_report = csv_importer(file_path)
    elif file_extension == 'json':
        inv_report = json_importer(file_path)
    elif file_extension == 'xml':
        inv_report = xml_importer(file_path)
    return inv_report


def csv_importer(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = reader(csv_file, delimiter=',')
        list_of_rows = list(csv_reader)
        inv_report = inv_lst_converter(list_of_rows)
    return inv_report


def json_importer(file_path):
    with open(file_path, 'r') as json_file:
        inv_report = json.load(json_file)
    return inv_report


def xml_importer(file_path):
    with open(file_path, 'r') as xml_file:
        content = xml_file.read()
        d = xmltodict.parse(content)
        group = [dict(i) for i in d['dataset']['record']]

    return group


def inv_lst_converter(rows):
    lst = []
    for index in range(1, len(rows)):
        item = {
            "id": rows[index][0],
            "nome_do_produto": rows[index][1],
            "nome_da_empresa": rows[index][2],
            "data_de_fabricacao": rows[index][3],
            "data_de_validade": rows[index][4],
            "numero_de_serie": rows[index][5],
            "instrucoes_de_armazenamento": rows[index][6]
        }

        lst.append(item)
    return lst
