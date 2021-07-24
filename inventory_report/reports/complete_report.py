from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list):

        simple_report = super().generate(list)

        company_name = [item["nome_da_empresa"] for item in list]

        counter_companies = Counter(company_name)

        quantity_product_company = ""
        for company in counter_companies:
            quantity_products = company_name.count(company)
            quantity_product_company += f"- {company}: {quantity_products}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa: \n"
            f"{quantity_product_company}"
        )
