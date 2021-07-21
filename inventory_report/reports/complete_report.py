from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_report = super().generate(data)

        companies_names = Counter(
          company["nome_da_empresa"] for company in data
        )

        companies_format = [
          f"- {key}: {value}" for key, value in companies_names.items()
        ]

        return (
          f"{simple_report}\n"
          "Produtos estocados por empresa: \n"
          + "\n".join(companies_format)
          + "\n"
        )
