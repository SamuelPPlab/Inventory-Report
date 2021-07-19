from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list_dict):
        list_oldest_date = sorted(
            list_dict, key=lambda i: (i["data_de_fabricacao"]), reverse=False
        )
        list_oldest_date_value = list_oldest_date[0]["data_de_fabricacao"]

        list_current_validate = sorted(
            list_dict,
            key=lambda i: (i["data_de_validade"]),
            reverse=False,
        )

        list_current_validate_sort = [
            item["data_de_validade"]
            for item in list_current_validate
            if item["data_de_validade"] > str(date.today())
        ]
        list_current_validate_value = list_current_validate_sort[0]

        list_names = dict()
        for product in list_dict:
            if not list_names.get(product["nome_da_empresa"]):
                list_names[product["nome_da_empresa"]] = 1
            else:
                list_names[product["nome_da_empresa"]] += 1

        name_company_highest_qtd_products = sorted(
            list_names.items(), key=lambda x: x[1], reverse=True
        )[0][0]
        # print(name_company_highest_qtd_products)

        message = (
            f"Data de fabricação mais antiga: {list_oldest_date_value}\n"
            f"Data de validade mais próxima: {list_current_validate_value}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{name_company_highest_qtd_products}\n"
        )
        # print(message)
        return message


if __name__ == "__main__":

    # RETORNO
    # Data de fabricação mais antiga: YYYY-MM-DD
    # Data de validade mais próxima: YYYY-MM-DD
    # Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

    LIST_EXAMPLE = [
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
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]

    # simple_report = SimpleReport()
    # simple_report.generate(LIST_EXAMPLE)

    # print(SimpleReport.generate(LIST_EXAMPLE))
