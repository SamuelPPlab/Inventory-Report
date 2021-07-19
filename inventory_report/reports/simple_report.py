from datetime import datetime
from statistics import mode


class SimpleReport:
    def date_is_future(date_str):
        return datetime.strptime(date_str, "%Y-%m-%d") > datetime.today()

    def generate(list):
        oldest = min(product["data_de_fabricacao"] for product in list)

        first_to_expire = min(
            product["data_de_validade"]
            for product in list
            if SimpleReport.date_is_future(product["data_de_validade"])
        )

        most_frequent_company = mode(
            product["nome_da_empresa"] for product in list
        )

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {first_to_expire}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{most_frequent_company}\n"
        )
