#3)Password 
import re 
def Validate_password(str): 
 p = re.compile("^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-
={}]).{8,}$") 
 if (str == None): 
 return False 
 if(re.search(p, str)): 
 return True 
 else: 
 return False 
 
str1 = "Pass@123" 
if(Validate_password(str1)): 
 print("Password is valid.") 
else: 
 print("Password is invalid.")