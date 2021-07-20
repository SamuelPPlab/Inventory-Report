from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Generate_Report:
    def generate(lista, tipo_de_relatorio):
        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(lista)
        if tipo_de_relatorio == "completo":
            return CompleteReport.generate(lista)


class Serialize:
    def xml_to_list(data):
        lista = []
        for item in data:
            empresa = {}
            empresa["id"] = item[0].text
            empresa["nome_do_produto"] = item[1].text
            empresa["nome_da_empresa"] = item[2].text
            empresa["data_de_fabricacao"] = item[3].text
            empresa["data_de_validade"] = item[4].text
            empresa["numero_de_serie"] = item[5].text
            empresa["instrucoes_de_armazenamento"] = item[6].text
            lista.append(empresa)
        return lista


class Inventory:
    def import_data(path, tipo_de_relatorio):
        if path.split(".")[1] == "csv":
            with open(path, mode="r") as arquivo:
                reader = csv.DictReader(arquivo)
                lista = []
                for linha in reader:
                    lista.append(linha)
            return Generate_Report.generate(lista, tipo_de_relatorio)

        if path.split(".")[1] == "json":
            with open(path, mode="r") as arquivo:
                lista = json.load(arquivo)
            return Generate_Report.generate(lista, tipo_de_relatorio)

        if path.split(".")[1] == "xml":
            with open(path, mode="r") as arquivo:
                tree = ET.parse(arquivo)
                data = tree.getroot()
            lista = Serialize.xml_to_list(data)
            return Generate_Report.generate(lista, tipo_de_relatorio)
