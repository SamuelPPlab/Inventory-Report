from datetime import datetime


class SimpleReport:

    def generate(list):
        today_date = datetime.today().strftime('%Y-%m-%d')
        manufacturing_date = min(
            item["data_de_fabricacao"] for item in list
        )
        expiration_date = min(
            item["data_de_validade"] for item in list
            if item["data_de_validade"] >= today_date
        )
        company = max(
            item["nome_da_empresa"] for item in list
        )

        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
