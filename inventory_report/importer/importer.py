from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self):
        print("Importer")

    @abstractmethod
    def import_data(self):
        raise NotImplementedError
