import datetime


class SimpleReport:
    def __init__(self):
        pass

    @staticmethod
    def generate(lista):
        data_de_fabricacao_mais_antiga = str(datetime.date.today())
        for objeto in lista:
            data_da_vez_bruta = objeto["data_de_fabricacao"]  #.split("-")
            data_da_vez = datetime.date(
                int(data_da_vez_bruta[0]),
                int(data_da_vez_bruta[1]),
                int(data_da_vez_bruta[2]),
            )

            data_antiga_bruta = data_de_fabricacao_mais_antiga  #.split("-")
            data_antiga = datetime.date(
                int(data_antiga_bruta[0]),
                int(data_antiga_bruta[1]),
                int(data_antiga_bruta[2]),
            )

            if data_antiga > data_da_vez:
                data_de_fabricacao_mais_antiga = data_da_vez

        return data_de_fabricacao_mais_antiga


if __name__ == "__main__":
    data = [
        {"data_de_fabricacao": "2020-07-04"},
        {"data_de_fabricacao": "2019-07-04"},
        {"data_de_fabricacao": "2018-07-04"},
    ]
    print(SimpleReport.generate(data))
# # [

#   {
#     "id": 1,
#     "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#     "nome_da_empresa": "Forces of Nature",
#     "data_de_fabricacao": "2020-07-04",
#     "data_de_validade": "2023-02-09",
#     "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#     "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#   }
# ]

