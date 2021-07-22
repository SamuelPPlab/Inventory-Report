from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def doCounter(data):
        text = ''
        counter = Counter(product["nome_da_empresa"] for product in data)
        for attr, value in counter.items():
            text = text + f"- {attr}: {value}\n"
        return (f"Produtos estocados por empresa: \n{text}")

    @classmethod
    def generate(cls, data):
        return super().generate(data) + "\n" + CompleteReport.doCounter(data)
