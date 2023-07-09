#2. Write a program to calculate factorial of a given number 
#using recursion
def factorial(n): 
 if n == 0:
  return 1 
 else:
  return n*factorial(n-1)
num = int(input("Enter the number: ")) 
result = factorial(num) 
print("Factorial is:", result)
