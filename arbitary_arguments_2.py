# Python program to illustrate **kwargs for variable number of keyword arguments 

def myfun(**kwargs) : 
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# driven code 
        myfun(first = "geeks", mid = "for", last = "geeks")