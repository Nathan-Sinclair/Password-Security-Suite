def password_length_check(password): 
# Defines a function to determine the length of the user's password; takes the password as an argument
    i = 0
    for char in password:
        i = i + 1
    return i
    #Tracks and returns the digit count of the password