import re

def password_characterclass_check(password):
# Defines a function that evaluates the users password and returns the count of unique character classes 
    Uppercase = False
    Lowercase = False
    Symbol = False
    Digit = False
    numberofclasses = 0

    for char in password: 
        if re.search(r'[A-Z]', char):
            Uppercase = True
        if re.search(r'[a-z]', char): 
            Lowercase = True
        if re.search(r'[^\w\s]', char): 
            Symbol = True
        if re.search(r'\d', char): 
            Digit = True

    if Uppercase == True:
        numberofclasses += 1
    if Lowercase == True:
        numberofclasses += 1
    if Symbol == True:
        numberofclasses += 1
    if Digit == True:
        numberofclasses += 1
    # Iterates through the password string and counts each time a unique character class is identified 

    return numberofclasses 

