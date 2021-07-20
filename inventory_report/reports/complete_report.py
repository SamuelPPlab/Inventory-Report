from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        first_part = super().generate(list)

        products_by_company = Counter(
            product["nome_da_empresa"] for product in list
        ).items()

        second_part_list = [
            f"- {key}: {value}" for key, value in products_by_company
        ]

        second_part = (
            "Produtos estocados por empresa: \n"
            + "\n".join(second_part_list)
            + "\n"
        )

        return f"{first_part}" "\n" f"{second_part}"
