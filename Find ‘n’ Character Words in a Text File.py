n=5
2. f=open("demo", "r")
3. words=f.read().split()
4. n_char_words = [word for word in words if len(word) == n] 
5. 
6. print(f"{n}-character words:", n_char_words) 
7. 
8. f.close()