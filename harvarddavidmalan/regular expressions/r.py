"""
#Regular expressions
email = input("Whats your email ? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

import re 

email = input("Whats your email ?").strip()

if re.search(".+@.+.edu", email):  #here accept jorge@recceba?edu
    print("Valid")
else:
    print("Invalid")    

#Raw String
import re     

email = input("Whats your email?").strip()

if re.search(r".+@\.edu", email):
    print("Valid")
else:
    print("Invalid")    

#3    
import re 

email = input("Whats your email?").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")    #^ - start of the string 
                        #$ - matches the end of the string or the newline at the end of the string 
#4                   
import re  

email = input("Whats your email?").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")    

#5  
import re  

email = input("Whats your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): #agora temos caracteres de a e z , entre 0 e 9
    print("Valid")
else:
    print("Invalid")    

import re   

email = input("Whats your email? ").strip()

if re.search(r"^\w+@\.edu$"):
    print("Valid")
else:
    print("Invalid")    

#\w ---[a-zA-Z0-9]
#\d -- decimal digit
#\s whitespace characters
#\S not whitespace characters 
#\w word character 
#\W not a word character 

"""
import re   

email = input("Whats your email?")

if re.search(r"^\w+@\w.+\.(com|net|edu|gov|org)"):  #pode se utilizar tambem A|B, (...), (?:....)
    print("Valid")
else:
    print("Invalid")    

