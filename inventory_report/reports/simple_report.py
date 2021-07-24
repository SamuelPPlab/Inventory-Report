from statistics import mode
from datetime import datetime


class SimpleReport:
    def generate(products):
        hash = "YHgWQGD8ZeExU9Lez_IIekqBfXcquHAgG0rj9v0mXf0"
        print(hash)
        oldest_product = min(
            product["data_de_fabricacao"] for product in products
        )

        next_to_expire = min(
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"]
            > datetime.today().strftime("%Y-%m-%d")
        )

        common_company = mode(
            product["nome_da_empresa"] for product in products
        )

        report = (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {next_to_expire}\n"
            "Empresa com maior quantidade de "
            f"produtos estocados: {common_company}\n"
        )
        return report
