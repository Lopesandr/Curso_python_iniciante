from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def tipo_animal(tipo):
       print(tipo)

class Circle(Animal):
    pass

if __name__ == '__main__': 
    Circle.tipo_animal('Cachorro')