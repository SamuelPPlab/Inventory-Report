from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(list):
        today = datetime.today().strftime("%Y-%m-%d")

        oldest_fabrication_date = min(
            product["data_de_fabricacao"] for product in list
        )

        closest_expiration_date = min(
            product["data_de_validade"] for product in list
            if product["data_de_validade"] > today
        )

        c_name = Counter(
            company["nome_da_empresa"] for company in list
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {c_name}\n"
        )


# Luciano Berchon e Pedro Riso
