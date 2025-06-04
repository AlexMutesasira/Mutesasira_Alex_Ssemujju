# Abstraction
# Abstract classes are classes that cannot be instantiated, they are used to define a common interface for a group of related classes.
# Abstact class and interfaces

# A class that contains one or more methods 

# you need to first import the ABC and the abstract method from the abc module

from abc import ABC, abstractmethod

# starting a car engine and bike
# Define abstract class
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # this method has no implementation
    
    # child class implementing the abstract method 
    
class car(vehicle):
        def start(self):
            print('The car engine has started')
            
    # derived class implementing the abstract method
    
class bike(vehicle):
        def start(self):
            print('The bike engine has started')
            
# note we cannot create an object of an abstract class . This would raise an error
# we can only create objects of the subclasses

car1 = car()
car1.start()

bike1 = bike()
bike1.start()