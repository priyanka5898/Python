#Q 3. Write a program to perform following operaƟons on dicƟonary
#1. Check whether a given key exists in a dicƟonary or not.
demo = {"Parth": 10, "Yash": 23} 
if "bjvj" in demo: 
 print("Key exists") 
else: 
 print("Key not exists")

#2. Iterate over dicƟonary items using for loop.
my_dict = {"apple": 3, "banana": 2, "orange": 1} 
for key, value in my_dict.items(): 
 print(f"{key}: {value}")

# 3. Concatenate two dicƟonaries to create one
 
dict_1 = {'Parth': 15, 'Yash': 10, 'Sandesh' : 12 } 
dict_2 = {'Chaitali': 18,'RiƟka': 20,'Akshta' : 16 }
dict_3 = {**dict_1,**dict_2} 
print(dict_3) 

#4. Sum all the values of a dicƟonary
 
dict1={"pen":100,"pencil":90,"eraser":50,"marker":110} 
print(dict1) 
print("sum:",sum(dict1.values())) 
 
# 5. Get the maximum and minimum value of dicƟonary.
 
marks={"Parth":17,"Yash":18,"Sandesh":20} 
count=marks.values() 
maximum=max(count) 
minimum=min(count) 
 
print("maximum=",maximum) 
maximum= 20 
 
print("minimum=",minimum) 
minimum= 17 