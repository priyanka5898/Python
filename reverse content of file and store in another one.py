f=open("Demo3","w")
2. f.write("Throtal!!")
3. f.close 
4. 
5. source="Demo.txt"
6. destination="Demo3.txt"
7. f=open(source,"r")
8. f3=open(destination,"a")
9. content=f.read()
10. reversed_content=content[::-1]
11. f3.write(reversed_content)
12. print("Done!!")