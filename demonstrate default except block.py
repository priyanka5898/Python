#D] Write Python program to demonstrate default except block. 
try: 
 x = int(input("Enter a number: ")) 
 y = int(input("Enter another number: ")) 
 result = x / y 
 print("The result of the division is:", result) 
except ValueError: 
 print("Invalid input. Please enter an integer.") 
except ZeroDivisionError: 
 print("Error: division by zero.") 
 except: 
 print("An unknown error occurred.") 