from abc import ABC, abstractmethod
from datetime import datetime


class Report(ABC):
    @abstractmethod
    def generate(data: list[dict]) -> str:
        raise NotImplementedError


def extract_dates(data: list[dict], key: str) -> list[datetime]:
    return [datetime.strptime(item[key], "%Y-%m-%d") for item in data]


def count_occurrences(data: list[dict]) -> list[dict]:
    return [(category, data.count(category)) for category in data]


class SimpleReport(Report):
    @staticmethod
    def generate(data: list[dict]) -> str:
        manufacturing_dates: list[datetime] = extract_dates(
            data, key="data_de_fabricacao"
        )
        earliest_manufacturing_date: str = min(manufacturing_dates).strftime(
            "%Y-%m-%d"
        )

        expiration_dates: list[datetime] = extract_dates(
            data, key="data_de_validade"
        )
        now = datetime.now()
        closest_expiration_date: str = min(
            date for date in expiration_dates if date > now
        ).strftime("%Y-%m-%d")

        company_names: list[str] = [item["nome_da_empresa"] for item in data]
        company_occurrences_names: list[tuple] = count_occurrences(
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
