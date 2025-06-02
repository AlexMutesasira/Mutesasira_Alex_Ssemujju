# list and dictionary comprehension
# list comprehension

square = [x**2 for x in range(10)]
print (square)

numbers =[1,2,3,4,5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)

# List comprehension with condition
#must be even numbers

even_square =[x**2 for x in range(10) if x % 2 == 0]
print(even_square)