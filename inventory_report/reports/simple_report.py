""" import json """
from datetime import datetime
from operator import itemgetter
from collections import Counter

""" with open(
  "/home/cezar/trybe-projects/
  Computer Science/sd-07-inventory-report/inventory_report/data/inventory.json"
  ) as file:
    inventory = json.load(file) """


class SimpleReport:
    def __init__(self):
        print("Simple Report criado")

    @classmethod
    def get_older_fab_date(cls, list):
        olderDate = sorted(list, key=itemgetter("data_de_fabricacao"))[0]
        return olderDate["data_de_fabricacao"]

    @classmethod
    def get_closest_expiration_date(cls, list):
        format_date = "%Y-%m-%d"
        return str(
            min(
                datetime.strptime(item["data_de_validade"], format_date)
                for item in list
                if datetime.strptime(item["data_de_validade"], format_date)
                > datetime.today()
            ).date()
        )

    @classmethod
    def amount_of_stocked_products(cls, list):
        all_companies = []
        for company in list:
            all_companies.append(company["nome_da_empresa"])

        commom_companies = Counter(all_companies).most_common()
        return commom_companies[0][0]

    @classmethod
    def generate(cls, list):
        older_fab_date = cls.get_older_fab_date(list)
        closest_expiration_date = cls.get_closest_expiration_date(list)
        company_greatest_amount = cls.amount_of_stocked_products(list)

        simple_report = (
            f"Data de fabricação mais antiga: {older_fab_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_greatest_amount}\n"
        )
        return simple_report
