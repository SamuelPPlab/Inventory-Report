from collections import Counter
from inventory_report.reports.simple_report import SimpleReport

# complete_report
# Complete_report


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, dataList):
        companies = dict(Counter(data["nome_da_empresa"] for data in dataList))
        companies_products = "".join(
            f"- {data[0]}: {data[1]}\n" for data in companies.items()
        )

        return (
            f"{super().generate(dataList)}\n"
            "Produtos estocados por empresa: \n"
            f"{companies_products}"
        )
