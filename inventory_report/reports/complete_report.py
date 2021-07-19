from inventory_report.reports.simple_report import SimpleReport
# https://docs.python.org/3/library/collections.html?highlight=counter#collections.Counter
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_inventory):
        simple_report = SimpleReport.generate(product_inventory)
        companys = [
          company["nome_da_empresa"] for company in product_inventory
        ]
        number_of_companys = Counter(companys)
        company_stock = ''
        for company in number_of_companys:
            company_stock += f"- {company}: {number_of_companys[company]}\n"
        complete_report = (
          f"{simple_report}"
          "\n"
          f"Produtos estocados por empresa: \n"
          f"{company_stock}"
        )
        return complete_report
