from inventory_report.reports.simple_report import SimpleReport
from string import Template
from collections import Counter


class CompleteReport(SimpleReport):

    complete_report_template = Template(
        "\nProdutos estocados por empresa: \n$content\n"
    )

    @classmethod
    def generate(cls, product_list):

        content = "\n".join(
            [
                f"- {company}: {qty}"
                for company, qty in (
                    Counter(
                        product["nome_da_empresa"] for product in product_list
                    ).items()
                )
            ]
        )

        return super().generate(
            product_list
        ) + cls.complete_report_template.substitute(content=content)
