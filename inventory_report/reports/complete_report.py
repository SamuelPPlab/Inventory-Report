from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        simpleReport = SimpleReport.generate(list)

        companiesProducts = Counter(
            product["nome_da_empresa"] for product in list
        ).items()

        companiesProductsReport = ""
        for key, value in companiesProducts:
            companiesProductsReport += f"- {key}: {value}\n"

        return (
          f"{simpleReport}\n"
          + "Produtos estocados por empresa: \n"
          + f"{companiesProductsReport}"
        ) 
