import datetime
from typing import Counter


class SimpleReport():
    def getOldestManufacturingDate(report_list):
        oldestDate = datetime.date.today()

        for report in report_list:
            if (
                datetime.date.fromisoformat(
                    report['data_de_fabricacao']
                ) < oldestDate
            ):
                oldestDate = datetime.date.fromisoformat(
                    report['data_de_fabricacao']
                )

        return oldestDate.isoformat()

    def getClosestValidDate(report_list):
        closest_valid_date = datetime.date.max
        today = datetime.date.today()

        for report in report_list:
            if (
                datetime.date.fromisoformat(
                    report['data_de_validade']
                ) > today
            ):
                if (
                    datetime.date.fromisoformat(
                        report['data_de_validade']
                    ) < closest_valid_date
                ):
                    closest_valid_date = datetime.date.fromisoformat(
                        report['data_de_validade']
                    )

        return closest_valid_date

    def getCompanyWithMoreProducts(report_list):
        companies = []

        for report in report_list:
            companies.append(report['nome_da_empresa'])

        return Counter(companies).most_common()

    @classmethod
    def generate(cls, report_list):
        oldest_manufacturing_date = cls.getOldestManufacturingDate(
            report_list
        )
        closest_valid_date = cls.getClosestValidDate(report_list)
        company_with_more_products = cls.getCompanyWithMoreProducts(
            report_list
        )

        return (
            f'Data de fabricação mais antiga: {oldest_manufacturing_date}\n'
            + f'Data de validade mais próxima: {closest_valid_date}\n'
            + 'Empresa com maior quantidade de produtos estocados: '
            + f'{company_with_more_products[0][0]}\n'
        )
