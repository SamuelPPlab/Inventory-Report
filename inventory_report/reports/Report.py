from abc import ABC, abstractmethod
from datetime import datetime


class Report(ABC):
    @abstractmethod
    def generate(data: list[dict]) -> str:
        raise NotImplementedError

    @staticmethod
    def extract_dates(
        data: list[dict], key: str, format: str = "%Y-%m-%d"
    ) -> list[datetime]:
        return [datetime.strptime(item[key], format) for item in data]

    @staticmethod
    def count_occurrences(data: list[dict]) -> list[dict]:
        items = []
        for item in data:
            element = (item, data.count(item))
            if element not in items:
                items.append(element)
        return items
