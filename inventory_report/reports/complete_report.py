from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_dict):
        simple_report = super().generate(list_dict)
        # print(simple_report)

        company_products = super()._generate_name_company(list_dict, False)
        # print(tupla_company_products)

        message_products = ""
        for item in company_products:
            message_products += f"- {item}: {company_products[item]}\n"
        # print(message_products)

        message = (
          f"{simple_report}\n"
          "Produtos estocados por empresa: \n"
          f"{message_products}"
        )
        return message


if __name__ == "__main__":

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

#     Data de fabricação mais antiga: YYYY-MM-DD
#     Data de validade mais próxima: YYYY-MM-DD
#     Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

#     Produtos estocados por empresa:
#     - Physicians Total Care, Inc.: QUANTIDADE
#     - Newton Laboratories, Inc.: QUANTIDADE
#     - Forces of Nature: QUANTIDADE

    # print(CompleteReport.generate(LIST_EXAMPLE))
