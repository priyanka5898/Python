A] Write Python program to demonstrate the following:
 1. SyntaxError 
 2. TypeError 
 3. IndexError 
 4. ValueError 
 5. ZeroDivisionError 
 6. fileNotFound 
 1. SyntaxError 
print("Hello world!) # missing closing quotaƟon mark will result in a syntax error
 2. TypeError 
x = 5 
y = "2" 
z = x + y # adding an integer and a string will result in a type error 
 3. IndexError 
my_list = [1, 2, 3] 
print(my_list[3]) # trying to access an index that is out of range will result in an index error 
4. ValueError 
user_input = input("Enter a number: ") 
num = int(user_input) # if the user enters a non-numeric value, trying to convert it to an int will result in a value error 
 5. ZeroDivisionError 
x = 5 
y = 0 
z = x/y # dividing by zero will result in a zerodivision error 
6. FileNotFoundError 
with open("nonexistent_file.txt") as f: # trying to open a file that doesn't exist will result in a file not found error 
 data = f.read() 