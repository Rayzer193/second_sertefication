from tabulate import tabulate

from model.pack_animals import Horses, Camels, Donkeys
from model.pets import Cats, Dogs, Hamsters


class RegistryAnimals:

    def __init__(self):
        self.__log_registry = []

    def get_log_registry(self):
        return self.__log_registry

    def number_of_animals(self):
        return len(self.__log_registry)

    def __add_cat(self, name, command, birth_date, id_animal=None):
        cat = Cats(id_animal, name, command, birth_date)
        self.__log_registry.append(cat)

    def __add_dog(self, name, command, birth_date, id_animal=None):
        dog = Dogs(id_animal, name, command, birth_date)
        self.__log_registry.append(dog)

    def __add_hamster(self, name, command, birth_date, id_animal=None):
        hamster = Hamsters(id_animal, name, command, birth_date)
        self.__log_registry.append(hamster)

    def __add_horse(self, name, command, birth_date, id_animal=None):
        horse = Horses(id_animal, name, command, birth_date)
        self.__log_registry.append(horse)

    def __add_camel(self, name, command, birth_date, id_animal=None):
        camel = Camels(id_animal, name, command, birth_date)
        self.__log_registry.append(camel)

    def __add_donkey(self, name, command, birth_date, id_animal=None):
        donkey = Donkeys(id_animal, name, command, birth_date)
        self.__log_registry.append(donkey)

    __function_add_animal = {'кошка': __add_cat, 'собака': __add_dog, 'хомяк': __add_hamster,
                             'лошадь': __add_horse, 'осёл': __add_donkey, 'верблюд': __add_camel}

    def add_animal(self, kind, name, command, birth_date):
        for key, value in self.__function_add_animal.items():
            if key == kind:
                value(self, name, command, birth_date)
                break

    @property
    def tabl_registry(self):
        """Формирует представление реестра в виде таблицы.:return: список всех животных в виде таблицы"""
        headers = ['№', 'Тип животного', 'Вид животного', 'Имя',
                   'Список команд', 'Дата рождения']
        tabl = [[i, animal.get_type_animals(),
                 animal.get_kind_animals(), animal.get_name(),
                 animal.get_command(), animal.get_birth_date()]
                for i, animal in enumerate(self.__log_registry, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')

    def list_kind_pets(self):
        kind_pets = set()
        for item in self.__log_registry:
            if item.get_id_type() == 1:
                kind_pets.add(item.get_kind_animals())
        return kind_pets

    def list_kind_pack(self):
        kind_pack = set()
        for item in self.__log_registry:
            if item.get_id_type() == 2:
                kind_pack.add(item.get_kind_animals())
        return kind_pack

    def find_animal(self, index):
        return self.__log_registry[index]

    def get_command(self, index):
        return self.__log_registry[index].get_command()

    def add_command(self, index, commands):
        self.__log_registry[index].add_command(commands)
