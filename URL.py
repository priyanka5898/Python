#1)URL 
import re 
def Validate_url(str): 
 p = re.compile("^hƩps?://[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$") 
 if (str == None): 
 return False 
 if(re.search(p, str)): 
 return True 
 else: 
 return False 
 
str1 = "hƩps://instagram.com"
if(Validate_url(str1)): 
 print("url is valid.") 
else: 
 print("url is invalid.") 
