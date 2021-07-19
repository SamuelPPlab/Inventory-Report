# -*- coding: utf-8 -*-
from collections import Counter

class SingleReport:
    @classmethod
    def generate(self, productsList):
        min_manufactured_date = min(pdt['data_de_fabricacao'] for pdt in productsList)
        closest_expiration_date = min(pdt['data_de_validade'] for pdt in productsList)

        companies = Counter(p['nome_da_empresa'] for p in productsList).most_common()

        return {
            'Data de fabricação mais antiga': min_manufactured_date,
            'Data de validade mais próxima': closest_expiration_date,
            'Empresa com maior quantidade de produtos estocados': companies[0][0]
        }
        

# pdtList = [
#     {
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#         "nome_da_empresa": "Aalbatroz",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#     },{
#         "id": 2,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#         "nome_da_empresa": "Ambar",
#         "data_de_fabricacao": "2020-07-02",
#         "data_de_validade": "2023-02-07",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#     },{
#         "id": 1,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#         "nome_da_empresa": "Ambar",
#         "data_de_fabricacao": "2020-07-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#     },{
#         "id": 2,
#         "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#         "nome_da_empresa": "Ambar",
#         "data_de_fabricacao": "2020-07-02",
#         "data_de_validade": "2023-02-07",
#         "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#         "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#     }
# ]
# print(SingleReport.generate(pdtList))