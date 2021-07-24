from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        res = super().generate(data)

        formato = "\n".join(
            [
                f"- {key}: {value}"
                for key, value in Counter(
                    list(map(lambda x: x["nome_da_empresa"], data))
                ).items()
            ]
        )

        return (
            f"{res}"
            "\n"
            "Produtos estocados por empresa: \n"
            f"{formato}"
            "\n"
        )
