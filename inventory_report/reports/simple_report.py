from datetime import datetime


class SimpleReport:
    def transform_date_format(string_date):
        return datetime.strptime(string_date, '%Y-%m-%d').date()

    def get_old_date(products):
        date_old = products[0]["data_de_fabricacao"]
        date_old = SimpleReport.transform_date_format(date_old)
        for product in products:
            date_now = SimpleReport.transform_date_format(
                product["data_de_fabricacao"]
            )
            if date_old > date_now:
                date_old = date_now
        return date_old.strftime("%Y-%m-%d")

    def count_quantity_name_company(companies):
        count_max_value = 0
        name_company = ""
        for company in companies:
            if companies.count(company) > count_max_value:
                name_company = company
                count_max_value = companies.count(company)
        return name_company

    def get_new_date(products):
        date_new = products[0]["data_de_validade"]
        date_new = SimpleReport.transform_date_format(date_new)
        for product in products:
            date_now = SimpleReport.transform_date_format(
                product["data_de_validade"]
            )
            if date_new < date_now:
                date_new = date_now
        return date_new.strftime("%Y-%m-%d")

    def mount_list_anythink(dict, key):
        list = []
        for item in dict:
            list.append(item[key])
        return list

    @staticmethod
    def generate(products):
        date_old = SimpleReport.get_old_date(products)
        date_new = SimpleReport.get_new_date(products)
        list_company = SimpleReport.mount_list_anythink(
            products, "nome_da_empresa"
        )
        company_name = SimpleReport.count_quantity_name_company(list_company)

        report = (
            f"Data de fabricação mais antiga: {date_old}\n"
            f"Data de validade mais próxima: {date_new}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {company_name}\n"
        )
        return report
'''
stock = [
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


report = SimpleReport.generate(stock)
print(report)
print("Data de fabricação mais antiga: 2019-09-13" in report)'''
