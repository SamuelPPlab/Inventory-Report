from datetime import datetime


class SimpleReport:
    def __init__(self, report):
        pass

    @classmethod
    def generate(cls, report):

        now = datetime.today()

        cls.antiga = min(
          [item["data_de_fabricacao"] for item in report]
        )
        cls.proxima = min(
          [
            datetime.strptime(item["data_de_validade"], '%Y-%m-%d')
            for item in report
          ], key=lambda x: abs(x - now))
        cls.quantidadeProdutos = max(
          [
            item["nome_da_empresa"]
            for item in report
          ], key=[item["nome_da_empresa"] for item in report].count
        )
        return (
              f"Data de fabricação mais antiga: {cls.antiga}\n"
              f"Data de validade mais próxima: {cls.proxima.date()}\n"
              f"Empresa com maior quantidade de produtos estocados: "
              f"{cls.quantidadeProdutos}\n"
        )
