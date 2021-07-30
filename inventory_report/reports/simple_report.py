from datetime import datetime
from statistics import mode


class SimpleReport:
    def expire_date(date):
        return datetime.strptime(date, "%Y-%m-%d") > datetime.today()

    def generate(list):
        oldest_product = min(product["data_de_fabricacao"] for product in list)

        first_product_expired = min(
            product["data_de_validade"]
            for product in list
            if SimpleReport.expire_date(product["data_de_validade"])
        )

        company_with_the_most_product_quantity = mode(
            ####
            product["nome_da_empresa"] for product in list
        )

        return (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {first_product_expired}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{company_with_the_most_product_quantity}\n"
        )
