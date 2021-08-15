# para gerar dado empresa com maior quantidade de produtos estocados:
# https://pt.stackoverflow.com/questions/407400/calcular-quantas-vezes-se-repetem-os-valores-dentro-de-uma-key-em-dicion%C3%A1rio-p

# para criar a logica de validades e fabricação
# https://stackoverflow.com/questions/59612212/find-latest-date-value-in-a-dictionary

from datetime import datetime


class SimpleReport:
    def generate(lista):
        ct = {}
        beta = datetime.max.date()
        gamma = datetime.max.date()
        for value in lista:
            # mostrar data sem horario, tipos datetime e date:
            # https://stackoverflow.com/questions/18039680/django-get-only-date-from-datetime-strptime
            df = datetime.strptime(
                value["data_de_fabricacao"], "%Y-%m-%d"
            ).date()
            dv = datetime.strptime(
                value["data_de_validade"], "%Y-%m-%d"
            ).date()
            print(dv)
            if df <= beta:
                beta = df
            if dv <= gamma and dv > datetime.now().date():
                gamma = dv
            if value["nome_da_empresa"] in ct:
                ct[value["nome_da_empresa"]] += 1
            else:
                ct[value["nome_da_empresa"]] = 1
        v = list(ct.values())
        k = list(ct.keys())
        # para alcançar o formato desejado:
        # https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
        return f"""Data de fabricação mais antiga: {beta}
Data de validade mais próxima: {gamma}
Empresa com maior quantidade de produtos estocados: {k[v.index(max(v))]}
"""
