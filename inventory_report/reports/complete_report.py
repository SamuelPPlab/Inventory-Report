from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    def __init__(self, data):
        self.data = data

    def generate(data):
        itemList = []
        for item in data:
            itemList.append(item['nome_da_empresa'])

        commonList = Counter(itemList)
        finalResultList = ['Produtos estocados por empresa: ']
        for element in commonList:
            finalResultList.append(
                # Ref: www.guru99.com/python-counter-collections-example.html
                f"- {'%s: %d' % (element, commonList[element])}"
            )
        finalResult = '\n'.join(finalResultList)

        return f"""{SimpleReport.generate(data)}
{finalResult}
"""
