from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def count_itens_list(list, item):
        return list.count(item)

    def delete_items_repeated_in_list(list):
        new_list = []
        for item in list:
            if item not in new_list:
                new_list.append(item)
        return new_list

    def amout_dic_quanty_companies(companies_not_repeat, companies):
        dic_companies = {}
        for company in companies_not_repeat:
            dic_companies[company] = CompleteReport.count_itens_list(
                companies, company
            )
        return dic_companies

    @classmethod
    def generate(self, products):
        report = super().generate(products)

        companies = super().mount_list_anythink(products, "nome_da_empresa")

        companies_not_repeat = CompleteReport.delete_items_repeated_in_list(
            companies
        )

        dic_companies = CompleteReport.amout_dic_quanty_companies(
            companies_not_repeat, companies
        )

        quant_nature = dic_companies['Forces of Nature']
        quant_sanofi = dic_companies['sanofi-aventis U.S. LLC']
        quant_newton = dic_companies['Newton Laboratories']

        company_report = (
            f"Produtos estocados por empresa: \n"
            f"- Forces of Nature: {quant_nature}\n"
            f"- sanofi-aventis U.S. LLC: {quant_sanofi}\n"
            f"- Newton Laboratories: {quant_newton}\n"
        )

        return report + "\n" + company_report
