from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, productsList):
        min_manufactured_date = min(
            pdt["data_de_fabricacao"] for pdt in productsList
        )
        closest_expiration_date = min(
            pdt["data_de_validade"]
            for pdt in productsList
            if pdt["data_de_validade"] > datetime.today().strftime("%Y-%m-%d")
        )
        companies = Counter(
            p["nome_da_empresa"] for p in productsList
        ).most_common()

        return (
            f"Data de fabricação mais antiga: {min_manufactured_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{companies[0][0]}\n"
        )
