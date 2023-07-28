from data.dbsqlite_manager import SqLiteManager
from model.registry_animals import RegistryAnimals
from presenter.presenter import Presenter
from view.console import Console


class Service:
    def __init__(self):
        self.registry = RegistryAnimals()
        self.view = Console()
        self.data = SqLiteManager('human_friends2.db')
        Presenter(self.view, self.registry, self.data)

    def start(self):
        self.view.start()
