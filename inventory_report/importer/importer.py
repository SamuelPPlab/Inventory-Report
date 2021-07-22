from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    # @classmethod
    def import_data(cls, path):  # , report_type):
        raise NotImplementedError
