from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Generate_Report:
    def generate(lista, tipo_de_relatorio):
        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(lista)
        if tipo_de_relatorio == "completo":
            return CompleteReport.generate(lista)


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
