from datetime import datetime


class SimpleReport:
    @staticmethod
    def discard_dates_below_today(str_date):
        """
            Função recebe uma data em formato String e retorna
            True se for uma data futura à data atual
        """
        today = datetime.now()
        return datetime.strptime(str_date, "%Y-%m-%d") > today

    @classmethod
    def generate(cls, data):
        manufacturing_date = []
        validation_date = []
        company_name = []

        for item in data:
            if cls.discard_dates_below_today(item["data_de_validade"]):
                validation_date.append(item["data_de_validade"])

            manufacturing_date.append(item["data_de_fabricacao"])
            company_name.append(item["nome_da_empresa"])

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(validation_date)}\n"
            f"Empresa com maior quantidade de produtos estocados:"
            f" {max(company_name)}\n"
        )
