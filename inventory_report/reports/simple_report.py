import datetime


class SimpleReport():
    def getOldestManufacturingDate(report_list):
        oldestDate = datetime.date.today()

        for report in report_list:
            if (
                datetime.date.fromisoformat(
                    report['data_de_fabricacao']
                ) < oldestDate
            ):
                oldestDate = datetime.date.fromisoformat(
                    report['data_de_fabricacao']
                )

        return oldestDate.isoformat()

    def getClosestValidDate(report_list):
        closest_valid_date = datetime.date.max
        today = datetime.date.today()

        for report in report_list:
            if (
                datetime.date.fromisoformat(
                    report['data_de_validade']
                ) > today
            ):
                if (
                    datetime.date.fromisoformat(
                        report['data_de_validade']
                    ) < closest_valid_date
                ):
                    closest_valid_date = datetime.date.fromisoformat(
                        report['data_de_validade']
                    )

        return closest_valid_date

    def getCompanyByName(self, company_list, company_name):
        for company in company_list:
            if company['name'] == company_name:
                return company

    def productsByCompany(self, report_list):
        products_by_company = []
        companies_names = []

        for report in report_list:
            if (report['nome_da_empresa'] in companies_names):
                company = self.getCompanyByName(
                    self,
                    products_by_company,
                    report['nome_da_empresa']
                )
                company['quantity'] += 1
            else:
                products_by_company.append({
                    'name': report['nome_da_empresa'],
                    'quantity': 1
                })
                companies_names.append(report['nome_da_empresa'])

        return products_by_company

    def getCompanyWithMoreProducts(self, report_list):
        bigger_quantity = 0
        products_by_company = self.productsByCompany(self, report_list)
        bigger_quantity_company = {}
 
        for company in products_by_company:
            if (company['quantity'] > bigger_quantity):
                bigger_quantity = company['quantity']
                bigger_quantity_company = company

        return bigger_quantity_company

    @classmethod
    def generate(cls, report_list):
        oldest_manufacturing_date = cls.getOldestManufacturingDate(
            report_list
        )
        closest_valid_date = cls.getClosestValidDate(report_list)
        company_with_more_products = cls.getCompanyWithMoreProducts(
            cls,
            report_list
        )['name']

        return (
            f'Data de fabricação mais antiga: {oldest_manufacturing_date}\n'
            + f'Data de validade mais próxima: {closest_valid_date}\n'
            + 'Empresa com maior quantidade de produtos estocados: '
            + f'{company_with_more_products}\n'
        )
