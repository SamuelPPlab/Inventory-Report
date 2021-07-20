from abc import ABC, abstractmethod


class InventoryIterator(ABC):
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def __next__(self):
        raise NotImplementedError
