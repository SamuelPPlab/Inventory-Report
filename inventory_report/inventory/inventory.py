import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def readCSV(self, caminho):
        with open(caminho) as arquivo:
            arquivoCSV = csv.DictReader(arquivo)
            return list(arquivoCSV)

    @classmethod
    def import_data(self, caminho, tipo):
        if caminho.endswith(".csv"):
            conteudo = self.readCSV(caminho)
        if tipo == "simples":
            relatorio = SimpleReport.generate(conteudo)
        else:
            relatorio = CompleteReport.generate(conteudo)
        return relatorio
