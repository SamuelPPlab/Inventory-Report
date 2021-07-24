from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):      

    @classmethod
    def generate(cls, products: list) -> str:
        sp_report = SimpleReport.generate(products)
        nome_empresas = []
        companies = ""
        for item in products:
            nome_empresas.append(item["nome_da_empresa"])
        for company in Counter(nome_empresas).items():
            companies += f"- {company[0]}: {company[1]}\n"

        return (
            f"{sp_report}\n"
            f"Produtos estocados por empresa: \n{companies}"
        )
