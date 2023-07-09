#3. Write a program to create decorators and generators
#Decorators
def decor(func):
 def inner(name):
  if name=="parth": 
   print("Hello, I am parth")
  else:
   func(name) 
 return inner
@decor
def outer(name):
 print("Hii", name, "How are you?")
outer("parth") 
outer("yash")
#Generators
def mygen():
 yield "50"
 yield "60"
 yield "70"
g=mygen() 
print(next(g)) 
print(next(g)) 
print(next(g))