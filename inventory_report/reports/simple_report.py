from datetime import datetime


# https://stackoverflow.com/questions/25002600/finding-min-max-date-with-list-comprehension-in-python
class SimpleReport:
    @staticmethod
    def findOldDate(element):
        return datetime.strptime(
            element["data_de_fabricacao"], "%Y-%m-%d"
        ).date()

    @staticmethod
    def findRecentDate(element):
        return datetime.strptime(
            element["data_de_validade"], "%Y-%m-%d"
        ).date()

    @staticmethod
    def findName(element):
        return element["nome_da_empresa"]

    @classmethod
    def generate(cls, dictionary):
        fabricacaoMaisVelha = list(map(cls.findOldDate, dictionary))
        mais_antigo = fabricacaoMaisVelha[0]
        for data in fabricacaoMaisVelha:
            if data < mais_antigo:
                mais_antigo = data

        validadeMaisProxima = list(map(cls.findRecentDate, dictionary))
        data_atual = datetime.now().date()
        acumulador_mais_recente = validadeMaisProxima[0] - data_atual

        for data in validadeMaisProxima:
            if acumulador_mais_recente > abs(data_atual - data):
                mais_recente = data

        empresaMaisEstoque = list(map(cls.findName, dictionary))

        return (
            f"Data de fabricação mais antiga: {mais_antigo}\n"
            f"Data de validade mais próxima: {mais_recente}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{max(empresaMaisEstoque)}\n"
        )
