from datetime import date
# https://docs.python.org/3/library/statistics.html#statistics.mode
from statistics import mode


class SimpleReport:
    @staticmethod
    def generate(product_inventory):
        older_fabrication = min(
          build_date["data_de_fabricacao"]
          for build_date in product_inventory
        )
        nearest_expiration = min(
          due_date["data_de_validade"]
          for due_date in product_inventory
          if due_date["data_de_validade"] > str(date.today())
        )
        bigger_stock = mode(
          company["nome_da_empresa"] for company in product_inventory
        )
        report_fabrication = (
          f"Data de fabricação mais antiga: {older_fabrication}"
        )
        report_expiration = (
          f"Data de validade mais próxima: {nearest_expiration}"
        )
        report_stock = (
          f"Empresa com maior quantidade de produtos estocados: {bigger_stock}"
        )
        simple_report = (
          f"{report_fabrication}\n{report_expiration}\n{report_stock}\n"
        )
        return simple_report
