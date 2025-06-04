# Inheritance
# Inheritance is a concept in object-oriented programming where a class inherits properties and behaviors from another class.
# The class that inherits is called the subclass (child class), and the class from which it inherits is called the superclass (parent class).
# The subclass inherits all the properties and behaviors of the superclass, and can also add its own unique properties and behaviors.

#superclass / parent class / base class
# an object is an instance of a class

class Animal:
    def speak(self): #self initialising methods
        print("The animal makes some good sound")
        
#sub class / child class / derived class

class cat(Animal):
    def sound(self):
        print('cat makes sound moew')
        
#create an object of cat
cat1 = cat()

#calling the inherited method
cat1.speak()

#calling the own method
cat1.sound()