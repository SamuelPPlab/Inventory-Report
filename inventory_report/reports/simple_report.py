import datetime


class SimpleReport:
    @staticmethod
    def manufacture_date(data):
        max_manufacture_date = datetime.timedelta.max
        for oldest_manufacture in data:
            if oldest_manufacture["data_de_fabricacao"] < max_manufacture_date:
                max_manufacture_date = oldest_manufacture["data_de_fabricacao"]
        return max_manufacture_date

    @staticmethod
    def validity(data):
        today = datetime.today().strftime("%Y-%m-%d")
        closest_validity = datetime.timedelta.max
        for validity in data:
            if validity["data_de_validade"] > today:
                if validity["data_de_validade"] < closest_validity:
                    closest_validity = validity["data_de_validade"]
        return closest_validity

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
