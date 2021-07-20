from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dictionaryList):
        reportDefault = super().generate(dictionaryList)
        return reportDefault + "\n" + cls.productsByEnterprise(
            dictionaryList
        )

    def productsByEnterprise(dataList):
        nameList = []
        [
            nameList.append(item["nome_da_empresa"])
            for item in dataList
            if item["nome_da_empresa"] not in nameList
        ]
        result = "Produtos estocados por empresa: \n"
        for name in nameList:
            qtd = len(
                list(
                    filter(
                        lambda data: data["nome_da_empresa"] == name,
                        dataList,
                    )
                )
            )
            result += f"- {name}: {qtd}\n"
        return result
