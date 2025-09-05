import math 
from collections import Counter 

def password_entropy_check(password): 
# Defines a function that checks entropy of the users password and returns a score in bits
    if not password: 
        return 0
        #this will return 0 bits for entropy if the string is empty
    
    charset_size = 0 
    symbols = r"!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~"
    if any(char.islower() for char in password): 
        charset_size += 26 

    if any(char.isupper() for char in password): 
        charset_size += 26    
 
    if any(char.isdigit() for char in password): 
        charset_size += 10 

    if any(char in symbols for char in password):     
        charset_size += 32  
    # The charset size is being calculated for the password, 
    # If specific character class is found in the password it will add all possible chars of that character class to the total once.

    return round(math.log2(charset_size) * len(password))
    # Using the calculated charset size for the password. Function returns the entropy of the password in bits in a rounded integer

