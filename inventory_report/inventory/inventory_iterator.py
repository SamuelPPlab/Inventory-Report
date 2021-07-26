from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.__inventory = inventory
        self.__index = 0

    def __next__(self):
        try:
            current_value = self.__inventory[self.__index]
        except IndexError:
            raise StopIteration()
        else:
            self.__index += 1
            return current_value
