from datetime import datetime
import json


class SimpleReport:
    def generate(lista):
        lista_empresas = lista

        quantidade_produtos = max(
            [item["nome_da_empresa"] for item in lista_empresas]
        )

        current_time = datetime.today().strftime("%Y-%m-%d")

        nearest_expiration_date = min(
            data["data_de_validade"]
            for data in lista_empresas
            if data["data_de_validade"] > current_time
        )

        oldest_date = min(
            data["data_de_fabricacao"] for data in lista_empresas
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {quantidade_produtos}\n"
        )


with open("./inventory_report/data/inventory.json") as file:
    result = file.read()
    lista = json.loads(result)
