# lambda function
# What is a lambda function?

# it is used for small functions, we use the lambda keyword

square = lambda x: x*x
print(square(5))

#Add lambda functions
add = lambda a,b: a+b
print(add(99,12))

#lambda functions are used for one time operations
# use lambda function to get square of list map [1,2,3,4,5]

number=[1,2,3,4,5]
squared=list(map(lambda x: x*x, number))
print(squared)