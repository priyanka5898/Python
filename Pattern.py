# Q5. Write a program to print following paƩerns
#1) 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
rows=4 
for i in range(1,rows+1): 
 for j in range(1,i+1): 
  print(j,end='') 
 print('') 

#2) 
# **** 
# *** 
# ** 
# * 
rows = 5 
for i in range(0, rows): 
 # nested loop for each column 
 for j in range(0, i + 1): 
 # print star 
  print("*", end=' ') 
 # new line aŌer each row
 print("\r") 
 
 
 
#3) 
# 55555 
# 4444 
# 333 
# 22 
# 1 
 
rows = 5 
# reverse loop 
for i in range(rows, 0, -1): 
 num = i 
 for j in range(0, i): 
  print(num, end=' ') 
 print("\r") 

#4) 
#A 
#BC 
#CDE 
#DEFG 
#EFGHI 
 
# Outer loop 
for i in range(65,70): 
 k=i 
 # Inner loop 
 for j in range(65,i+1): 
  print(chr(k),end="") 
 k=k+1 
 print()