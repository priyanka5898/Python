#Write Python program to handle multiple exceptions in single except block . 
try: 
 x = int(input("Enter a number: ")) 
 y = int(input("Enter another number: ")) 
 result = x / y 
 print("The result of the division is:", result) 
 except (ValueError, ZeroDivisionError): 
 print("An error occurred. Please make sure you entered two non-zero integers.")