from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, file):
        self.file = file

    @abstractmethod
    def import_data(file):
        pass
