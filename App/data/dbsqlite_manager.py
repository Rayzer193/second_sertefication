import sqlite3

from model.pack_animals import Horses, Camels, Donkeys
from model.pets import Cats, Dogs, Hamsters
from model.registry_animals import RegistryAnimals


class SqLiteManager:
    def __init__(self, path: str):
        self.__path = path

    def __read_cat(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM cats")
            rows = cursor.fetchall()
            for row in rows:
                cat = Cats(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(cat)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_dog(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM dogs")
            rows = cursor.fetchall()
            for row in rows:
                dog = Dogs(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(dog)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_hamster(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM hamsters")
            rows = cursor.fetchall()
            for row in rows:
                hamster = Hamsters(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(hamster)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_horse(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM horses")
            rows = cursor.fetchall()
            for row in rows:
                horse = Horses(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(horse)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_camel(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM camels")
            rows = cursor.fetchall()
            for row in rows:
                camel = Camels(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(camel)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_donkey(self, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_animal, name, command, birth_date FROM donkeys")
            rows = cursor.fetchall()
            for row in rows:
                donkey = Donkeys(row[0], row[1], row[2], row[3])
                log_registry.get_log_registry().append(donkey)
            return "Успешно"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    __function_read_animal = [__read_cat, __read_dog, __read_hamster,
                              __read_horse, __read_donkey, __read_camel]

    def read_db(self, log_registry: RegistryAnimals):
        result = "Успешно"
        for item in self.__function_read_animal:
            result = item(self, log_registry)
            if result.startswith('Ошибка'):
                return result
        return result

    __dict_kinds = {'кошка': 'cats', 'собака': 'dogs', 'хомяк': 'hamsters',
                    'лошадь': 'horses', 'осёл': 'donkeys', 'верблюд': 'camels'}

    def save_animal(self, type_id, kind, name, command, birth_date):
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            data = (type_id, name, command, birth_date)
            cursor.execute(f"INSERT INTO {self.__dict_kinds[kind]} (type_id, name, command, birth_date) "
                           "VALUES (?, ?, ?, ?)", data)
            connect.commit()
            return "Запись добавлена в базу данных"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def save_command(self, index, log_registry: RegistryAnimals):
        cursor = None
        connect = None
        kind = self.__dict_kinds[log_registry.get_log_registry()[index].get_kind_animals()]
        id_animal = log_registry.get_log_registry()[index].get_id_animal()
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute(f"UPDATE {kind} SET command = ? WHERE id_animal = ?",
                           (log_registry.get_command(index), id_animal))
            connect.commit()
            return "Список команд успешно изменен."
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()
