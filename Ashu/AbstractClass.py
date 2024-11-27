from abc import ABC, abstractmethod

# Creating an abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Subclassing the abstract class
class Dog(Animal):
    def make_sound(self):
        print("Woof")

    def move(self):
        print("Dog is running")

# Creating an instance of the subclass
dog = Dog()
dog.make_sound()  # Output: Woof
dog.move()        # Output: Dog is running

# Trying to instantiate the abstract class would raise an error
# animal = Animal()  # This will raise TypeError: Can't instantiate abstract class Animal with abstract methods make_sound, move
