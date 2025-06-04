# polymorphism
# same method name can behave differently depending on different objects

# polymorphism with inheritance
class bird:
    def fly(self):
        print('birds take water but they dont urinate')
        
# derived class 

class eagle(bird):
    def fly(self):
        print('eagles have a long life span')
       
class sparrow(bird):
    def fly(self):
            print('Sparrows fly at low altitude')
            
# how we use polymophism

def flight_test(bird):
    bird.fly() #run respective class method based on an object
    
#create objects
eagle1 =eagle()
sparrow1 =sparrow()
    
#passing objects to the function
flight_test(eagle1)
flight_test(sparrow1)

#call the flight test method