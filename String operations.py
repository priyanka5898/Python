#Q2. Write a program to perform following operaƟons on string
#1. Reverse string. 
#SOL
String = "Hey Python"[::-1] 
print(String) 

#2. Count vowels and consonants in a string. 
#sol
str=input("type anything: "); 
vowels=0 
consonants=0 
for i in str: 
 if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or 
 i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ): 
  vowels=vowels+1; 
 
 else: 
  consonants=consonants+1; 
 
 
print("vowels:",vowels); 
print("consonant:",consonants); 

#3. Count the number of leƩers in a word.
#sol
word= "Python" 

print (len('word')) 
#4. Convert lower leƩer to upper and upper leƩer to lower in a string.
#sol
name = "PaRth DesHpAndE" 
# lower to upper and upper to lower 
print(name.swapcase()) 

#5. Count lower, upper, numeric and special characters in a string. 
#sol
str="pa@12" 
upper=0; 
lower=0 
num=0 
specialchar=0 
for i in range(len(str)): 
 if(str[i].isupper()): 
  upper=upper+1 
 elif(str[i].islower()): 
  lower=lower+1 
 elif(str[i].isdigit()): 
  num=num+1 
 else: 
  specialchar=specialchar+1 
 print("upper=",upper) 
 print("lower=",lower) 
 print("num=",num) 
 print("specialchar=",specialchar)