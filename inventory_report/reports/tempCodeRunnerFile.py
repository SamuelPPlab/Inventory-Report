from string import Template
from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    this_template = Template("\nProdutos estocados por empresa: \n$result\n")
    a = Counter(item["nome_da_empresa"] for item in list).items()
    print(a)
    
    @classmethod
    def generate(cls, list):
        result = "\n".join(
            [
                f"- {empresa}: {quantidade}"
                for empresa, quantidade in (
                    Counter(item["nome_da_empresa"] for item in list).items()
                )
            ]
        )

        return super().generate(list) + cls.this_template.substitute(
            result=result
        )
