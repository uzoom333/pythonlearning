"""
import re  

email = input("What's your email? ")

if re.search(r"^\w+@\w.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")    
"""    
#
import re  

email = input("What's your email? ")

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid") 

#also all this valid not all the checking necessary to check if a email is valid , have re.match/re.fullmatch    