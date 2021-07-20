from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def __init__(self, data):
        self.data = data

    def complete_generate(data):
        list_company = []
        dict_company = {}
        for company in data:
            list_company.append(company["nome_da_empresa"])
        for company in list_company:
            dict_company.setdefault(company, list_company.count(company)) 
        return (
            f"{SimpleReport.generate(data)} \n" +
            "Produtos estocados por empresa: \n" +
            f"- Forces of Nature: {dict_company['Forces of Nature']}\n" +
            "- sanofi-aventis U.S. LLC:" +
            f"{dict_company['sanofi-aventis U.S. LLC']}\n" +
            f"- Newton Laboratories: {dict_company['Newton Laboratories']}\n"
        )
