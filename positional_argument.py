# Python program to demonstrate positional arguments 
def nameAge(name, age) :
    print("Hi, I'm ", name)
    print("My age is ", age)

# You will get correct output because argument is not in order 
    print("\n Case - 1 : ")
    nameAge("Suraj", 27)

# You will get correct output because argument is not in order  
    print("\n Case - 2 : ")
    nameAge(27, "Suraj")

