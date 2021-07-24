from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(path_document):
        raise NotImplementedError
