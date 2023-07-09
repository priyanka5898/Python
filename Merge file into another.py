f=open("Demo.txt","r")
2. f2=open("Demo2","r")
3. f3=open("merged", "w")
4. f3.write(f.read())
5. f3.write(f2.read())
6. print("Files merged successfully.")
7. f.close 
