#B] Write Python program to raise user defined exception. 
class JustExcepƟon(ExcepƟon):
 def __init__(self, message): 
  print(message) 
 raise JustExcepƟon("Raise an ExcepƟon")
try: 
 raise JustExcepƟon("Raise an ExcepƟon")
except ExcepƟon as e:
 print("ExcepƟon Raised")