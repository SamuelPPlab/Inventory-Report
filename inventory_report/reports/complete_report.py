from typing import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dictionary):
        result = super().generate(dictionary)
        empresaMaisEstoque = list(map(cls.findName, dictionary))
        result2 = dict(Counter(empresaMaisEstoque))
        formated_result = "\nProdutos estocados por empresa: \n"
        for key, item in result2.items():
            formated_result += f"- {key}: {item}\n"

        return result + formated_result
