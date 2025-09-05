import os

def password_commonpassword_check(password, filepath=None): 
# Defines a function that checks if the users password matches any of the passwords in the rockyou.txt list

    if filepath is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))  
        filepath = os.path.join(script_dir, "rockyou.txt")
    # Checks the directory of this .py file for rockyou.txt

    password = password.strip() 
  
    try: 
        with open(filepath, 'r', encoding='latin-1', errors='ignore') as file: 
            for line in file: 
                if password == line.strip(): 
                    return True 
        return False 
        # Iterating through rockyou.txt and comparing each password with the users password
        # Returns True if a match is found and returns False if no matches are found
    
    except Exception as e: 
        print(f"Error opening local file: {e}") 
        return False
        # Catches any error while opening/reading the file, prints the error message, and safely returns False
