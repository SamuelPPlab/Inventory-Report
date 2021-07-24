from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = cls.generate(products)
        report_tail = "Produtos estocados por empresa:\n"
        all_companies = [product["nome_da_empresa"] for product in products]
        companies = list(set(all_companies))
        for company in companies:
            report_tail


