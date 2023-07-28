from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def set_presenter(self, presenter):
        """Aбстрактный метод, который реализует понимание экземпляр класса-презентера."""

    @abstractmethod
    def start(self):
        """Aбстрактный метод, который реализует начальную настройку консольного приложения и запускает его отображение."""
        