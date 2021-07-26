from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
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
        most_commom_companies = cls.productsByCompany(
            cls,
            report_list
        )

        company_list = ''
        for company in most_commom_companies:
            company_list += f'- {company["name"]}: {company["quantity"]}\n'

        return (
            f'Data de fabricação mais antiga: {oldest_manufacturing_date}\n'
            + f'Data de validade mais próxima: {closest_valid_date}\n'
            + 'Empresa com maior quantidade de produtos estocados: '
            + f'{company_with_more_products}\n\n'
            + 'Produtos estocados por empresa: \n'
            + company_list
        )
