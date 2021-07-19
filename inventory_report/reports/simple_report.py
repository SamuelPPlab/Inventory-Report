from datetime import datetime
import json


class SimpleReport:
    def generate(lista):
        listas_empresas = lista

        quantidadeProdutos = max(
            [item["nome_da_empresa"] for item in listas_empresas]
        )

        current_time = datetime.today().strftime("%Y-%m-%d")

        nearest_expiration_date = min(
            data["data_de_validade"]
            for data in listas_empresas
            if data["data_de_validade"] > current_time
        )

        oldest_date = min(
            data["data_de_fabricacao"] for data in listas_empresas
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {quantidadeProdutos}\n"
        )


with open("./inventory_report/data/inventory.json") as file:
    result = file.read()
    lista = json.loads(result)


print(SimpleReport.generate(lista))
