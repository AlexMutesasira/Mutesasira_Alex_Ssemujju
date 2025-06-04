# Return values
# Return statement
# A function can return a value to the caller using a return statement 
# A return statement ends the function execution and sends the value back.

# return multiple values

def get_stats(a ,b):
    return a + b, a - b
sum_value, subtract_value = get_stats(20 ,12)
print('sum:', sum_value)
print('subtract:', subtract_value)

# Exercise 2

def divide_numbers(x,y):
    return x/y
print(divide_numbers(50,10))