from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, reportList):
        empresas = dict(Counter(
            data["nome_da_empresa"] for data in reportList))
        produtosPorEmpresas = "".join(
            f"- {data[0]}: {data[1]}\n" for data in empresas.items()
        )
        return (
            f"{super().generate(reportList)}\n"
            "Produtos estocados por empresa: \n"
            f"{produtosPorEmpresas}"
        )
