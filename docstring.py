# Python program to perform docstring

# defining a function
def evenodd(x) :
    """function to check if the number is even or odd """

    if(x%2 == 0):
        print("Even")

    else :
        print("Odd")
# printing docstring
print(evenodd.__doc__)

# calling a function 
evenodd(10)