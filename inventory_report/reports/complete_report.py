from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)

        count_companies_products = Counter(
            product["nome_da_empresa"] for product in data
        ).items()

        companies_report_list = [
            f"- {key}: {value}"
            for key, value
            in count_companies_products
        ]

        companies_report_string = "\n".join(companies_report_list)

        return (
            f"{simple_report}"
            "\n"
            "Produtos estocados por empresa: \n"
            f"{companies_report_string}"
            "\n"
        )
