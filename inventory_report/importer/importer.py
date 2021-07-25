from abc import ABC, abstractmethod


class Importer(ABC):

    @staticmethod
    def import_data(self, arq):
        raise NotImplementedError
