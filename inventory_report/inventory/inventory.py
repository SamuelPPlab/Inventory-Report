from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    def import_data(path, tipo_de_relatorio):
        with open(path, mode="r") as arquivo:
            reader = csv.DictReader(arquivo)
            lista = []
            for linha in reader:
                lista.append(linha)
        if tipo_de_relatorio == "simples":
            return SimpleReport.generate(lista)
        if tipo_de_relatorio == "completo":
            return CompleteReport.generate(lista)
