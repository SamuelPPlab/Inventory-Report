from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):
        earliest_manufacturing_date = min(
            item["data_de_fabricacao"] for item in list
        )

        closest_expiration_date = min(
            item["data_de_validade"] for item in list
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            >= datetime.now())

        companies = [item["nome_da_empresa"] for item in list]

        company_greatest_products, _ = Counter(companies).most_common()[0]

        return (
          f"Data de fabricação mais antiga: {earliest_manufacturing_date}\n"
          + f"Data de validade mais próxima: {closest_expiration_date}\n"
          + "Empresa com maior quantidade de produtos estocados: "
          + f"{company_greatest_products}\n"
        )
