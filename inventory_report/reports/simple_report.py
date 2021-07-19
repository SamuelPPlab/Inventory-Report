from datetime import date
from collections import Counter


class SimpleReport:
    def generate(data_dict):
        oldest_manufacture_date = min(
            [
                date.fromisoformat(data["data_de_fabricacao"])
                for data in data_dict
            ]
        )

        validate_date_list = [
            date.fromisoformat(data["data_de_validade"]) for data in data_dict
        ]
        validate_date_list.sort()
        closest_validate_date = [
            date for date in validate_date_list if date >= date.today()
        ]

        company_name_list = [data["nome_da_empresa"] for data in data_dict]
        company_name_counter = dict(Counter(company_name_list))
        company_name_sorted = sorted(
            company_name_counter.items(),
            key=lambda item: item[1],
            reverse=True,
        )
        # https://careerkarma.com/blog/python-sort-a-dictionary-by-value/

        report = (
            f"Data de fabricação mais antiga: {oldest_manufacture_date}\n"
            f"Data de validade mais próxima: {closest_validate_date[0]}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {company_name_sorted[0][0]}\n"
        )
        return report
