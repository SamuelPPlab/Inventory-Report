from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, item):
        companies = dict(Counter(data["nome_da_empresa"] for data in item))
        str_companies = "".join(
            f"- {data[0]}: {data[1]}\n" for data in companies.items()
        )
        return (
            f"{super().generate(item)}\n"
            "Produtos estocados por empresa: \n"
            f"{str_companies}"
        )
