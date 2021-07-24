from statistics import mode
from datetime import date


class SimpleReport:

    def generate(products):

        oldest_product = min(
            product["data_de_fabricacao"] for product in products
        )

        next_to_expire = max(
            product["data_de_validade"] for product in products
        )

        common_company = mode(
            product["nome_da_empresa"] for product in products
        )

        report = (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {next_to_expire}\n"
            "Empresa com maior quantidade de "
            f"produtos estocados: {common_company}"
        )
        return report
