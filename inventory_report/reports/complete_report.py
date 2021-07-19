# from datetime import datetime
from inventory_report.reports.simple_report import SimpleReport
from functools import reduce


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data: list[dict]) -> str:
        simple_report = SimpleReport.generate(data)
        company_names: list[str] = [item["nome_da_empresa"] for item in data]
        occurrences_names: list[tuple] = SimpleReport.count_occurrences(
            company_names
        )
        stocked_of_compay: set[str] = [
            f"- {company[0]}: {company[1]}\n" for company in occurrences_names
        ]

        return reduce(
            lambda accumulator, current: accumulator + current,
            stocked_of_compay,
            simple_report + "\nProdutos estocados por empresa: \n",
        )
