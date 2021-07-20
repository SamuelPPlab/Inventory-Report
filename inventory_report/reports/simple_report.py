from statistics import mode
from datetime import datetime


class SimpleReport:
    def verify_date(date_string):
        date_today = datetime.today()
        date_number = datetime.strptime(date_string, "%Y-%m-%d")
        return date_number > date_today

    def generate(item):
        company = [attribute["nome_da_empresa"] for attribute in item]
        initial_date = [attribute["data_de_fabricacao"] for attribute in item]
        final_date = [
            attribute["data_de_validade"] for attribute in item
            if SimpleReport.verify_date(attribute["data_de_validade"])
        ]

        format = (
            f"Data de fabricação mais antiga: {min(initial_date)}\n"
            f"Data de validade mais próxima: {min(final_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{mode(company)}\n"
        )

        return format
