from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def get_stock(self, data):
        list_name_enterprise = [
            data_report["nome_da_empresa"] for data_report in data
        ]
        enterprise_number_product = Counter(list_name_enterprise)
        enterprise_number_tuplas = (
            enterprise_number_product.items()
        )
        string_referent = "\nProdutos estocados por empresa: \n"
        for loop in enterprise_number_tuplas:
            index_tuplas = f"- {loop[0]}: {loop[1]}\n"
            string_referent += index_tuplas
        return string_referent

    @classmethod
    def generate(cls, data):
        generate = super().generate(data)
        stock = CompleteReport.get_stock(data)
        return generate + stock
