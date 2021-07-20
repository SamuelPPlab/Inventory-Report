from datetime import date


class SimpleReport(dict):

    def generate(list):
        dates = []
        expiration_date = []
        max_stock = []
        for item in list:
            dates.append(item['data_de_fabricacao'])
            if date.today() < date.fromisoformat(item['data_de_validade']):
                expiration_date.append(item['data_de_validade'])
            max_stock.append(item['nome_da_empresa'].strip())

        result_max_stock = max(set(max_stock), key=max_stock.count)
        old_date = min(dates)
        closest_date = min(expiration_date)
        return (
            f'Data de fabricação mais antiga: {old_date}\n' +
            f'Data de validade mais próxima: {closest_date}\n' +
            'Empresa com maior quantidade de ' +
            f'produtos estocados: {result_max_stock}\n')
