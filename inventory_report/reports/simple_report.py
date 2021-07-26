from datetime import datetime


class SimpleReport:
    def transform_date_format(string_date):
        return datetime.strptime(string_date, '%Y-%m-%d').date()

    def get_old_date(products):
        date_old = products[0]["data_de_fabricacao"]
        date_old = SimpleReport.transform_date_format(date_old)
        for product in products:
            date_now = SimpleReport.transform_date_format(
                product["data_de_fabricacao"]
            )
            if date_old > date_now:
                date_old = date_now
        return date_old.strftime("%Y-%m-%d")

    def count_quantity_name_company(companies):
        count_max_value = 0
        name_company = ""
        for company in companies:
            if companies.count(company) > count_max_value:
                name_company = company
                count_max_value = companies.count(company)
        return name_company

    def get_new_date(products):
        date_actual = datetime.today().date()

        count_diff_date = 1000
        date_validate = ""

        for product in products:
            date_currence = SimpleReport.transform_date_format(
                product["data_de_validade"]
            )
            if date_currence > date_actual:
                diff_dates = (date_currence - date_actual).days
                if (diff_dates) < count_diff_date:
                    date_validate = date_currence
                    count_diff_date = diff_dates

        return date_validate.strftime("%Y-%m-%d")

    @staticmethod
    def mount_list_anythink(dict, key):
        list = []
        for item in dict:
            list.append(item[key])
        return list

    @staticmethod
    def generate(products):
        date_old = SimpleReport.get_old_date(products)
        date_new = SimpleReport.get_new_date(products)
        list_company = SimpleReport.mount_list_anythink(
            products, "nome_da_empresa"
        )
        company_name = SimpleReport.count_quantity_name_company(list_company)

        report = (
            f"Data de fabricação mais antiga: {date_old}\n"
            f"Data de validade mais próxima: {date_new}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {company_name}\n"
        )
        return report
