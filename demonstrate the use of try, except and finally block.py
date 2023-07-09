#C] Write Python program to demonstrate the use of try, except and finally block
class JustExcepƟon(ExcepƟon):
 def __init__(self, message): 
  print(message) 
 raise JustExcepƟon("Raise an ExcepƟon")
try: 
 raise JustExcepƟon("Raise an ExcepƟon")
except ExcepƟon as e:
 print("ExcepƟon Raised")