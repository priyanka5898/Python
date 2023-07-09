file_path = "Demo.txt"
2. key = "key"
3. value = "value"
4. count = 0 
5. 
6. f=open("Demo", "r")
7. lines =f.readlines()
8. for line in lines:
9. if key in line and value in line:
10. count += 1 
11. 
12. print("Number of occurrences:", count)
13. f.close 
