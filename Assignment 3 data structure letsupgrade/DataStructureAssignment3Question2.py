#Question 2
#Define a function swap that should swap two values and print the swapped variables outside the swap function
#PROGRAM-
def swap(a, b):
    t = a
    a = b
    b = t
    return a, b
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a, b = swap(a, b)
print("Swapped value of first number is %d & second number is %d" %(a,b))