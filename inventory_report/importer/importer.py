from abc import abstractmethod, ABC


class Importer(ABC):
    @abstractmethod
    def import_data(path):
        raise NotImplementedError
