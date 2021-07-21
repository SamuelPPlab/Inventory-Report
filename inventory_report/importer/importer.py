from abc import ABC, abstractmethod
# https://programadoresbrasil.com.br/2021/04/classe-abstrata-em-python-entenda-como-funcionam/
# https://qastack.com.br/programming/2052390/manually-raising-throwing-an-exception-in-python


class Importer(ABC):

    @abstractmethod
    def import_data(cls, path_file):
        raise NotImplementedError
