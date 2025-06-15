from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getDetails(self):
        pass

    def getAge(self):
        return f"{self.__age}"

    def setAge(self, age):
        if age !=0 :
            self.__age = age
        else:
            raise ValueError("Age cannot be negatif")

    