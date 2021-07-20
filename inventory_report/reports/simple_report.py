from datetime import date
from statistics import mode


class SimpleReport():
    @staticmethod
    def generate(lista):
        fabrication_date = '2021-07-20'
        exp_date = '2045-07-20'
        empresas = []
        for item in lista:
            current_date = date.fromisoformat(item["data_de_fabricacao"])
            curr_exp = date.fromisoformat(item["data_de_validade"])
            if(current_date < date.fromisoformat(fabrication_date)):
                fabrication_date = item["data_de_fabricacao"]
            expiration = date.fromisoformat(exp_date)
            if(curr_exp > date.today() and curr_exp < expiration):
                exp_date = item["data_de_validade"]
            empresas.append(item["nome_da_empresa"])
        nome_empresa = mode(empresas)
        return(
            f"Data de fabricação mais antiga: {fabrication_date}\n"
            f"Data de validade mais próxima: {exp_date}\n"
            "Empresa com maior quantidade de"
            f" produtos estocados: {nome_empresa}\n"
            )
