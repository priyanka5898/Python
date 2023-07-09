
from math import * 
import random as r 
import datetime as d
#Math 
print(sqrt(100)) 
print(pow(4,2)) 
print(floor(3.5)) 
print(ceil(4.8))
#Random 
print(r.random()) 
print(r.randint(15,25))
print(r.randrange(10,30,2)) 
list = [23,17,5,4,1,30]
print(r.choice(list))
#Datetime
var = d.datetime.now() 
print(var.strftime("%D")) 
print(var)
