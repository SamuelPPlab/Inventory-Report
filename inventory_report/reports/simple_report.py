import datetime


class SimpleReport:
    @staticmethod
    def manufacture_date(data):
        max_manufacture_date = datetime.datetime.max
        for oldest_manufacture in data:
            if (
                datetime.datetime.strptime(
                    oldest_manufacture["data_de_fabricacao"], "%Y-%m-%d"
                )
                < max_manufacture_date
            ):
                max_manufacture_date = datetime.datetime.strptime(
                    oldest_manufacture["data_de_fabricacao"], "%Y-%m-%d"
                )
        return max_manufacture_date.date()

    @staticmethod
    def validity(data):
        today = datetime.datetime.today()
        closest_validity = datetime.datetime.max
        for validity in data:
            if (
                datetime.datetime.strptime(
                    validity["data_de_validade"], "%Y-%m-%d"
                )
                > today
            ):
                if (
                    datetime.datetime.strptime(
                        validity["data_de_validade"], "%Y-%m-%d"
                    )
                    < closest_validity
                ):
                    closest_validity = datetime.datetime.strptime(
                        validity["data_de_validade"], "%Y-%m-%d"
                    )
        return closest_validity.date()

    @staticmethod
    def company_with_more_itens(data):
        company = max([name["nome_da_empresa"] for name in data])
        return company

    @staticmethod
    def generate(data):
        max_manufacture_date = SimpleReport.manufacture_date(data)
        closest_validity = SimpleReport.validity(data)
        company_name = SimpleReport.company_with_more_itens(data)
        return (
            "Data de fabricação mais antiga: %s\n"
            "Data de validade mais próxima: %s\n"
            "Empresa com maior quantidade de produtos estocados: %s\n"
            % (max_manufacture_date, closest_validity, company_name)
        )
