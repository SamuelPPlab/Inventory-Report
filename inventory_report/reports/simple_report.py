import statistics
from statistics import mode


class SimpleReport:
    def generate(data):
        initial_date = [atribute["data_de_fabricacao"] for atribute in data]
        final_date = [atribute["data_de_validade"] for atribute in data]
        company = [atribute["nome_da_empresa" ] for atribute in data]

        format = (
            f"Data de fabricação mais antiga: {min(initial_date)}\n"
            f"Data de validade mais próxima: {max(final_date)}\n" # esse aqui tá errado :(
            f"Empresa com maior quantidade de produtos estocados: {mode(company)}\n"
        )

        return format
