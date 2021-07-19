from datetime import datetime


class SimpleReport:
    def __init__(self, mock):
        pass

    def generate(mock):

        now = datetime.today()

        antiga = min(
          [item["data_de_fabricacao"] for item in mock]
        )
        proxima = min(
          [
            datetime.strptime(item["data_de_validade"], '%Y-%m-%d')
            for item in mock
          ], key=lambda x: abs(x - now))
        quantidadeProdutos = max(
          [
            item["nome_da_empresa"]
            for item in mock
          ], key=[item["nome_da_empresa"] for item in mock].count
        )
        return (
              f"Data de fabricação mais antiga: {antiga}\n"
              f"Data de validade mais próxima: {proxima.date()}\n"
              f"Empresa com maior quantidade de produtos estocados: "
              f"{quantidadeProdutos}\n"
        )
