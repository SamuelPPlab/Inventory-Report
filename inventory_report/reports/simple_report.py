from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(dictionaryList):
        oldFab = sorted(
            dictionaryList,
            key=lambda data: data["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]
        nextVal = SimpleReport.orderOldFab(dictionaryList)
        best = SimpleReport.defineBest(dictionaryList)
        return (
            f"Data de fabricação mais antiga: {oldFab}\n"
            f"Data de validade mais próxima: {nextVal}\n"
            f"Empresa com maior quantidade de produtos estocados: {best}\n"
        )

    @staticmethod
    def orderOldFab(dataList):
        filteredList = filter(
            lambda data: datetime.now()
            < datetime.strptime(data["data_de_validade"], "%Y-%m-%d"),
            dataList,
        )
        orderedList = sorted(
            list(filteredList),
            key=lambda data: datetime.strptime(
                data["data_de_validade"], "%Y-%m-%d"
            )
            - datetime.now(),
        )
        return orderedList[0]["data_de_validade"]

    @staticmethod
    def defineBest(dataList):
        repetitions = 0
        result = {}
        for item in dataList:
            parameter = len(
                list(filter(
                    lambda data: data["nome_da_empresa"]
                    == item["nome_da_empresa"],
                    dataList,
                ))
            )
            if parameter > repetitions:
                repetitions = parameter
                result = item
        return result["nome_da_empresa"]
