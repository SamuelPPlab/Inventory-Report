from datetime import datetime
from operator import itemgetter
from collections import Counter


class SimpleReport:
    def __init__(self):
        print("Criando Simple Report")

    @staticmethod
    def get_oldest_product(list):
        olderDate = sorted(list, key=itemgetter("data_de_fabricacao"))[0]
        return olderDate["data_de_fabricacao"]

    @staticmethod
    def get_closest_expiration_date(list):
        format_date = "%Y-%m-%d"
        return str(
            min(
                datetime.strptime(item["data_de_validade"], format_date)
                for item in list
                if datetime.strptime(item["data_de_validade"], format_date)
                > datetime.today()
            ).date()
        )

    @staticmethod
    def amount_of_stocked_products(list):
        all_companies = []
        for company in list:
            all_companies.append(company["nome_da_empresa"])

        commom_companies = Counter(all_companies).most_common()
        return commom_companies[0][0]

    @classmethod
    def generate(cls, list):
        oldest_product = cls.get_oldest_product(list)
        closest_expiration_date = cls.get_closest_expiration_date(list)
        company_greatest_amount = cls.amount_of_stocked_products(list)

        simple_report = (
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_greatest_amount}\n"
        )
        return simple_report
