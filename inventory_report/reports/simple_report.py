from datetime import date
from collections import Counter


class SimpleReport:
    def __init__(self, data):
        self.data = data

    def generate(data):
        olderFab = date.today()
        today = date.today()
        daysToExp = 0
        result = ''
        namesCompany = []
        for item in data:
            dateFab = date.fromisoformat(item['data_de_fabricacao'])
            if (olderFab > dateFab):
                olderFab = dateFab

        for item in data:
            exDat = (date.fromisoformat(item['data_de_validade']) - today)
            if (daysToExp == 0 or daysToExp > exDat.days) and exDat.days > 0:
                daysToExp = exDat.days
                print(daysToExp)
                result = date.fromisoformat(item['data_de_validade'])

        for item in data:
            companyName = item['nome_da_empresa']
            namesCompany.append(companyName)
        companyName, _ = Counter(namesCompany).most_common()[0]

        return f"""Data de fabricação mais antiga: {olderFab}
Data de validade mais próxima: {result}
Empresa com maior quantidade de produtos estocados: {companyName}
"""

