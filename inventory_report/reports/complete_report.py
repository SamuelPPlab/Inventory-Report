from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        simple_reports = SimpleReport.generate(data)
        enterprises = [info["nome_da_empresa"] for info in data]
        enterprises_stock = Counter(enterprises)
        names = ''
        for info in enterprises_stock:
            names += f'- {info}: {enterprises_stock[info]}\n'
        return (
            f'{simple_reports}\n'
            f'Produtos estocados por empresa: \n{names}'
        )
