from datetime import datetime
from statistics import mode
from string import Template


class SimpleReport:
    template = Template(
        "Data de fabricação mais antiga: $data_mais_antiga\n"
        + "Data de validade mais próxima: $validade_mais_proxima\n"
        + "Empresa com maior quantidade de produtos estocados: "
        + "$empresa_com_mais_produtos\n"
    )

    @classmethod
    def generate(cls, lista):
        data_mais_antiga = min(item["data_de_fabricacao"] for item in lista)

        validade_mais_proxima = min(
            item["data_de_validade"]
            for item in lista
            if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        )

        empresa_com_mais_produtos = mode(
            item["nome_da_empresa"] for item in lista
        )

        return cls.template.substitute(
            data_mais_antiga=data_mais_antiga,
            validade_mais_proxima=validade_mais_proxima,
            empresa_com_mais_produtos=empresa_com_mais_produtos,
        )
