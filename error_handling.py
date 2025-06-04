# Python error handling
# define error
# Errors occur when a program encounters unexpected situations during execution

# types of errors
# 1: syntax error (when you violet the python syntax)
# 2: runtime error (eg 5/0  )
# 3: logical error

# deal with these kind of errors using blocks of code try ,except ,else and finally

# 1: try code expected to cause an error is put in here
# 2: except for handling the exceptions
# 3: else it runs if no exceptions occurs in the try block
# 4: finally code that executes whether the error occurs or not 

# example try to divide 5/0 (cause ZeroDivisionError)

try:
    result = 5/2
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print('Division success', result)
finally:
    print('Excecution completed')
    
# Exercise A custom exception that checks for a positive number .
