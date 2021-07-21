from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, list_dict):
        manufacturing_date_list = []
        expiration_date_list = []
        company_list = []

        for company in list_dict:
            manufacturing_date = datetime.strptime(
                company['data_de_fabricacao'], '%Y-%m-%d'
            )
            expiration_date = datetime.strptime(
                company['data_de_validade'], '%Y-%m-%d'
            )
            manufacturing_date_list.append(manufacturing_date)
            company_list.append(company['nome_da_empresa'])

            if expiration_date > datetime.now():
                expiration_date_list.append(expiration_date)

        manufacturing_date_list = sorted(manufacturing_date_list)
        expiration_date_list = sorted(expiration_date_list)
        company_list = Counter(company_list).most_common()
        manufacturing_date_one = manufacturing_date_list[0].strftime(
            '%Y-%m-%d'
        )
        expiration_date_one = expiration_date_list[0].strftime('%Y-%m-%d')
        company_name, _ = company_list[0]

        report = (
            f"Data de fabricação mais antiga: {manufacturing_date_one}\n"
            f"Data de validade mais próxima: {expiration_date_one}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_name}\n"
        )

        return report
