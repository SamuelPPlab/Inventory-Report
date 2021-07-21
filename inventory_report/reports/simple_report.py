from datetime import datetime


class SimpleReport:
    def generate(data):
        today = datetime.today().strftime("%Y-%m-%d")
        manufacturing_date = [info["data_de_fabricacao"] for info in data]
        validation_date = [info["data_de_validade"] for info in data]
        enterprises = [info["nome_da_empresa"] for info in data]

        oldest_date = min(manufacturing_date)
        closest_validate = min(
            [date for date in validation_date if date > today]
        )
        stock = max(enterprises, key=enterprises.count)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_validate}\n"
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )
