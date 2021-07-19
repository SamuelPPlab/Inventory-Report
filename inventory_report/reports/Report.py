from abc import ABC, abstractmethod
from datetime import datetime


class Report(ABC):
    @abstractmethod
    def generate(data: list[dict]) -> str:
        raise NotImplementedError

    def extract_dates(
        data: list[dict], key: str, format: str = "%Y-%m-%d"
    ) -> list[datetime]:
        return [datetime.strptime(item[key], format) for item in data]

    def count_occurrences(data: list[dict]) -> list[dict]:
        return [(category, data.count(category)) for category in data]
