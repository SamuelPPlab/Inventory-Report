# -*- coding: utf-8 -*-
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, productsList):
        min_manufactured_date = min(
            pdt['data_de_fabricacao']for pdt in productsList
        )
        closest_expiration_date = min(
            pdt['data_de_validade'] for pdt in productsList
        )

        companies = Counter(
            p['nome_da_empresa'] for p in productsList
        ).most_common()
        res = f'Data de fabricação mais antiga: {min_manufactured_date}' \
            f'Data de validade mais próxima: {closest_expiration_date}' \
            'Empresa com maior quantidade de produtos estocados: ' \
            f'{companies[0][0]}'
        return res
