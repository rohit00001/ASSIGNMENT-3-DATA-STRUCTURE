
#question 1
#Write a Python program to add two numbers using class and object.
#(Take both numbers as input from the user)class Test:


class Test :
    def findsum(self, a, b):
        s = a + b
        return s


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Test()
s = obj.findsum(a, b)

print("Sum is:", s)