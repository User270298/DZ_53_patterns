from abc import ABC, abstractmethod


class Data:
    _data = 0

    def __init__(self, value=0) -> None:
        Data._data += value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def __str__(self) -> str:
        return f"Текущая стоимость: {Data._data}"


class Addition(Data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def add(self, value):
        Data._data += value
        print("Выполняется добавление...")

    def __str__(self) -> str:
        return super().__str__()


class Subtraction(Data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def subtract(self, value):
        Data._data -= value
        print("Выполняется вычитание...")

    def __str__(self) -> str:
        return super().__str__()


class Command():
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AdditionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.add(self.value)

    def undo(self, commandObj):
        commandObj.set_command(SubtractionCommand(Subtraction(), self.value))
        commandObj.invoke()


class SubtractionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.subtract(self.value)

    def undo(self, commandObj):
        commandObj.set_command(AdditionCommand(Addition(), self.value))
        commandObj.invoke()


class ActionInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

    def undo(self):
        print("Oтменить ", end="")
        self.command.undo(self)


if __name__ == '__main__':
    obj = Data(40)
    print(obj)
    addition=Addition()
    substraction=Subtraction()
    command_addition = AdditionCommand(addition, 110)
    command_subtraction = SubtractionCommand(substraction, 50)

    action_invoker = ActionInvoker(command_addition)
    action_invoker.invoke()
    print(obj)

    action_invoker.set_command(command_subtraction)
    action_invoker.invoke()
    print(obj)

    action_invoker.undo()
    print(obj)
    action_invoker.undo()
    print(obj)

# Task 2
