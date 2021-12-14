from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  #property позволяет превратить метод класса в атрибут класса

    @abstractmethod  #Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  #Абстрактным называется объявленный, но не реализованный метод
    def telephone(self) -> None:  #телефон
        pass

    @abstractmethod
    def tablet(self) -> None:  #планшет
        pass

    @abstractmethod
    def laptop(self) -> None:  #ноутбук
        pass


class Technic_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Shop()

    @property  #property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def telephone(self) -> None:
        self._product.add("телефон")

    def tablet(self) -> None:
        self._product.add("планшет")

    def laptop(self) -> None:
        self._product.add("ноутбук")


class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  #property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  #применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Mvideo(self) -> None:
        self.builder.telephone()
        self.builder.tablet()

    def DNS(self) -> None:
        self.builder.laptop()
        self.builder.telephone()


if __name__ == "__main__":
    director = Director()
    builder = Technic_Builder()
    director.builder = builder

    print("М.Видео: ")
    director.Mvideo()
    builder.product.list_parts()

    print("\n\nDNS: ")
    director.DNS()
    builder.product.list_parts()
