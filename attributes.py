from typing import MutableMapping


class MyClass:
    def __init__(self) -> None:
        self._protected_attribute = 1
        self.__private_attribute = 1

    @classmethod
    def get_private_attribute(cls, instance):
        return instance.__private_attribute


foo = MyClass()
# print(foo.__private_attribute)
print(MyClass.get_private_attribute(foo))
print(foo.__dict__)
print(foo._MyClass__private_attribute)

class MyChildClass(MyClass):
    def __init__(self) -> None:
        super().__init__()

    def get_private_attribute(self):
        return self.__private_attribute

    def get_protected_attribute(self):
        return self._protected_attribute

bar = MyChildClass()
# print(bar.get_private_attribute())
print(bar.get_protected_attribute())
