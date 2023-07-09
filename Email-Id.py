#)Email-Id 
import re 
def Validate_email(str): 
 p = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$") 
 if (str == None): 
 return False 
 if(re.search(p, str)): 
 return True 
 else: 
 return False 
 
str1 = "abc@gamail.com" 
if(Validate_email(str1)): 
 print("email is valid.") 
else: 
 print("email is invalid.") 
