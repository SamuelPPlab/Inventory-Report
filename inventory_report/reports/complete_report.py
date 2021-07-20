from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def __init__(self):
        super().__init__(self)

    def generate(inv_products):
        simple_report = SimpleReport.generate(inv_products)
        most_common = inventory_per_company(inv_products)
        first_line = "Produtos estocados por empresa: "
        bottom_report = (f"""{first_line}
- {most_common[1][0]}: {most_common[1][1]}
- {most_common[0][0]}: {most_common[0][1]}
- {most_common[2][0]}: {most_common[2][1]}\n""")
        return simple_report + "\n" + bottom_report


def inventory_per_company(stock):
    lst = [item["nome_da_empresa"] for item in stock]
    report = Counter(lst)
    return report.most_common()
