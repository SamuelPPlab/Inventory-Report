from datetime import datetime


class SimpleReport:
    # def older_manufacturing(self, products):
    #     list_date = []
    #     for item in products:
    #         list_date.append(item["data_de_fabricacao"])
    #     old = min(list_date)
    #     return old

    # def nearest_expiration(self, products):
    #     today = datetime.now()
    #     list_validate = []
    #     for item in products:
    #         list_validate.append(item["data_de_validade"])
    #     validate = min(item for item in list_validate if item > str(today))
    #     return validate

    # def bigger_stock(self, products):
    #     list_company = []
    #     for item in products:
    #         list_company.append(item["nome_da_empresa"])
    #     counter = 0
    #     index = 0
    #     for item in list_company:
    #         if list_company.count(item) > counter:
    #             counter = list_company.count(item)
    #             index = list_company.index(item)
    #     return list_company[index]

    @classmethod
    def generate(self, products):
        list_date = []
        list_company = []
        today = datetime.now()
        list_validate = []
        result = []
        for item in products:
            list_date.append(item["data_de_fabricacao"])
            list_company.append(item["nome_da_empresa"])
            list_validate.append(item["data_de_validade"])
        old = min(list_date)
        validate = min(item for item in list_validate if item > str(today))
        counter = 0
        index = 0
        for item in list_company:
            if list_company.count(item) > counter:
                counter = list_company.count(item)
                index = list_company.index(item)
        result = (
            f"Data de fabricação mais antiga: {old}\n"
            f"Data de validade mais próxima: {validate}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{list_company[index]}\n"
        )
        return result
