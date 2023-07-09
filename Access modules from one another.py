#4. Create two different user defined modules and access 
#respective functions from one file to another
#Module1.py
def greet(name):
 print("Hello, " + name + "!") 
def square(x):
 return x**2
#Module2.py
import Module1
Module1.greet("parth") 
print(Module1.square(6))