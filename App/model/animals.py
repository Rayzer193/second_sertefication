from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, id_type, type_animals):
        self.__id_type = id_type
        self.__type_animals = type_animals

    @abstractmethod
    def get_id_type(self):
        """Абстрактный метод, который возвращает идентификатор типа животного"""

    @abstractmethod
    def get_type_animals(self):
        """Абстрактный метод, который возвращает описание типа животного"""
