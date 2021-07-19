from datetime import datetime
from inventory_report.reports.Report import Report


class SimpleReport(Report):
    @staticmethod
    def generate(data: list[dict]) -> str:
        manufacturing_dates: list[datetime] = Report.extract_dates(
            data, key="data_de_fabricacao"
        )
        earliest_manufacturing_date: str = min(manufacturing_dates).strftime(
            "%Y-%m-%d"
        )

        expiration_dates: list[datetime] = Report.extract_dates(
            data, key="data_de_validade"
        )
        now = datetime.now()
        closest_expiration_date: str = min(
            date for date in expiration_dates if date > now
        ).strftime("%Y-%m-%d")

        company_names: list[str] = [item["nome_da_empresa"] for item in data]
        company_occurrences_names: list[tuple] = Report.count_occurrences(
            company_names
        )
        company_occurrences_names.sort(
            key=lambda company: company[1], reverse=True
        )
        company_with_more_occurrences = company_occurrences_names[0][0]

        return (
            f"Data de fabricação mais antiga: {earliest_manufacturing_date}\n"
            + f"Data de validade mais próxima: {closest_expiration_date}\n"
            + "Empresa com maior quantidade de produtos estocados: "
            + company_with_more_occurrences
            + "\n"
        )
