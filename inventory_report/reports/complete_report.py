from datetime import datetime
from collections import Counter

data = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]


class CompleteReport:
    # def createText(products_by_company):
    #     for key, value in products_by_company.items():
    #         return f"- {key}: {value}"

    def generate(data):
        manufactoring_date = sorted(
            data, key=lambda data: data["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]

        current_date = datetime.now().date()
        data_sorted_validation = sorted(
            data,
            key=lambda data: current_date
            - datetime.strptime(data["data_de_validade"], "%Y-%m-%d").date(),
            reverse=True,
        )
        valid_dates = []
        for date in data_sorted_validation:
            if (
                datetime.strptime(date["data_de_validade"], "%Y-%m-%d").date()
                > current_date
            ):
                valid_dates.append(date)
        validation_date = valid_dates[0]["data_de_validade"]
        companies = []
        for item in data:
            companies.append(item["nome_da_empresa"])

        most_products_company = Counter(companies).most_common(1)[0][0]

        products_by_company = Counter(companies)
        products_text = ""
        for key, value in products_by_company.items():
            products_text += f"- {key}: {value}\n"

        response = (
            f"Data de fabricação mais antiga: {manufactoring_date}\n"
            f"Data de validade mais próxima: {validation_date}\n"
            "Empresa com maior quantidade de"
            f" produtos estocados: {most_products_company}\n\n"
            f"Produtos estocados por empresa: \n{products_text}"
        )

        return response
