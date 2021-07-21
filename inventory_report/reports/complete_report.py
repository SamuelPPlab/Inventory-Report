from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def __init__(self, data):
        self.data = data

    def generate(data):
        list_company = []
        dict_company = {}
        back_result = SimpleReport.generate(data)
        response = ''
        for company in data:
            list_company.append(company["nome_da_empresa"])
        for company in list_company:
            dict_company.setdefault(company, list_company.count(company))
        for key, value in dict_company.items():
            response += f"- {key}: {value}\n"
        result = (
            f"{back_result}\n"
            "Produtos estocados por empresa: \n"
            f"{response}"
        )
        return result
