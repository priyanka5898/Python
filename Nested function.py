#1. Write a program to demonstrate Nested function
num = int(input("Enter the number: ")) 
def outer_func():
 def inner_func():
  if num % 2 == 0:
   print("This is an even number") 
  else:
   print("This is an odd number") 
 inner_func()
outer_func()