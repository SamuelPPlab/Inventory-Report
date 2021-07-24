from inventory_report.reports.simple_report import SimpleReport
from functools import reduce
from typing import List, Set, Type, TypeVar

T = TypeVar('T', bound='CompleteReport')


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls: Type[T], data: List[dict]) -> str:
        old_info: str = SimpleReport.generate(data)

        company_names: List[str] = [
            attribute["nome_da_empresa"] for attribute in data
        ]

        company_quantities: List[tuple] = {
            name: company_names.count(name) for name in company_names
        }.items()

        new_info: Set[str] = [
            f"- {key}: {value}\n" for key, value in company_quantities
        ]

        result = reduce(
            lambda previous_info, current_info:
            previous_info + current_info,
            new_info,
            old_info + "\nProdutos estocados por empresa: \n"
        )
        return result


# Referências:
# https://pt.stackoverflow.com/questions/57513/funcionamento-classmethod
# https://docs.python.org/3/library/functions.html#classmethod
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
# https://stackoverflow.com/questions/39205527/can-you-annotate-return-type-when-value-is-instance-of-cls
# https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list
