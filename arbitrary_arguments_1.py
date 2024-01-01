# Python program to illustrate args for variable number of arguments 

def myfun(*argv) : 
    for a in argv:
        print(a)
        

myfun('Hello', 'Welcome', 'to', 'Geeks for geeks')