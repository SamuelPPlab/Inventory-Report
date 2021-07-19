import datetime


class SimpleReport:
    @staticmethod
    def compare_dates(date1, date2, closest=False):
        date_format = "%Y-%m-%d"
        if closest:
            actual_date = datetime.datetime.now()
            closest_expiration_date = datetime.datetime.strptime(
                date1, date_format
            )
            expiration_date = datetime.datetime.strptime(date2, date_format)
            if abs(closest_expiration_date - actual_date) > abs(
                expiration_date - actual_date
            ):
                closest_expiration_date = expiration_date
            return closest_expiration_date.strftime(date_format)
        else:
            oldest_manufacturing = datetime.datetime.strptime(
                date1, date_format
            )
            manufacturing_date = datetime.datetime.strptime(date2, date_format)
            if oldest_manufacturing.date() > manufacturing_date.date():
                oldest_manufacturing = manufacturing_date
            return oldest_manufacturing.strftime(date_format)

    @staticmethod
    def update_company_and_max_occurrences(
        actual_company,
        company_with_more_occurences,
        company_list,
        max_occurrences,
    ):
        number_of_occurrences = 1
        for dicts in company_list:
            if actual_company == dicts["nome_da_empresa"]:
                number_of_occurrences += 1
        if number_of_occurrences > max_occurrences:
            max_occurrences, company_with_more_occurences = (
                number_of_occurrences,
                actual_company,
            )
        return company_with_more_occurences, max_occurrences

    @staticmethod
    def generate(stock):
        company, max_occurrences = "", 0
        oldest_manufacturing, closest_expiration_date = (
            "2100-01-01",
            "1900-01-01",
        )
        for index, dictionary in enumerate(stock):
            oldest_manufacturing = SimpleReport.compare_dates(
                oldest_manufacturing, dictionary["data_de_fabricacao"]
            )
            closest_expiration_date = SimpleReport.compare_dates(
                closest_expiration_date, dictionary["data_de_validade"], True
            )
            (
                company,
                max_occurrences,
            ) = SimpleReport.update_company_and_max_occurrences(
                dictionary["nome_da_empresa"],
                company,
                stock[index + 1:],
                max_occurrences,
            )
        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )
