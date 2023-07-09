#Q1. Write a program to perform following operaƟons on list.
#1. Sum all the items in a list. 
#Sol- 
# create list
list1 = [4, 6, 1, 23, 11] 
total = sum(list1) 
# print total value
print("Sum of all item in given list: ", total) 

#2. Get the largest number from a list. 
#Sol- 
# list of numbers 
list1 = [16, 50, 9, 34, 90] 
list1.sort() 
# print the large number
print("Largest element is:", list1[-1]) 

#3. Remove duplicates from a list. 
#sol- 
#list 
list1 = [1, 5, 3, 6, 3, 5, 6, 1] 
print ("Original list: " 
 + str(list1)) 
list1 = list(set(list1)) 
print ("List aŌer removing duplicates : "
 + str(list1)) 
#4. Separate posiƟve and negaƟve number from a list.
#sol
list = [100, 50, 65, 82, 23,-21,-2,-15] 
print("Original list:"+ str(list)) 
list.sort() 
print("separated list:"+ str(list)) 
#5. Filter even and odd number from a list. 
#sol
nums = [13, 50, 73, 12, 53, 9, 1, 8] 
even = [] 
odd = [] 
for i in nums: 
 if(i % 2 == 0): 
  even.append(i) 
 else: 
  odd.append(i) 