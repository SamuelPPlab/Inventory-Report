from abc import ABC, abstractmethod


class Importer(ABC):

    @abstractmethod
    def import_data(self, arq):
        raise NotImplementedError

    def validate_extension(file_path, file_type):
        extension_file = file_path.split('.').pop()
        if extension_file != file_type:
            raise ValueError('Arquivo inválido')
