 f=open("Demo2","w")
2. f.write("You would like it!!")
3. f.close 
4. 
5. source="Demo.txt"
6. destination="Demo2.txt"
7. f=open(source,"r")
8. f2=open(destination,"a")
9. content= f.read()
10. f2.write(content)
11. print("Appended Successfully") 