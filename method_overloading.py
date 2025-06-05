# we deal with methods 
# methods carry parameters 
# methods are called 
# methods overloading , we have two or more methods having the same names but different kinds of parameters.

from multipledispatch import dispatch

@dispatch(int,int)
def sum(w,r):
    s=w+r
    print(s)


@dispatch(int,int,int)
def sum(w,r,x):
    s=w+r+x
    print(s)
sum(4,7)
sum(23,4,12)
