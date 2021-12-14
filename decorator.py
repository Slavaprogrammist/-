class Technic():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """
    def operation(self) -> str:
        pass


class Technic(Technic):
    """
       Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
       быть несколько вариаций этих классов.
       """
    def operation(self) -> str:
        return "Technic"


class Decorator(Technic):
    """Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    _component: Technic = None

    def __init__(self, component: Technic) -> None:
        self._component = component

    @property    #превращает метод класса в атрибут класса.
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Telephone(Decorator):
    def operation(self) -> str:
        return f"telephone({self.component.operation()})"


class Computer(Decorator):
    def operation(self) -> str:
        return f"computer({self.component.operation()})"


def show(component: Technic) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать простые компоненты
    simple = Technic()
    print("Client: I've got a simple component:")
    show(simple)
    print("\n")
    # и декорированные.
    #
    # Декораторы могут обёртывать не только простые
    # компоненты, но и другие декораторы.
    decorator1 = Telephone(simple)
    decorator2 = Computer(decorator1)
    print("Client: Now I've got a decorated component:")
    show(decorator2)