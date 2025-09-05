import secrets
import string
from Entropy_Calculation import password_entropy_check
from Common_Passwords import password_commonpassword_check
from Have_I_Been_Pwned import password_HIBP_check

def generate_secure_password():
# Defines a function that will generate a strong password
    
    while True:
        length = secrets.choice(range(12, 17))
      
        password_chars = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice(string.punctuation)
        ]
        # Length of the password is randomly decided to be between 12 and 17 and password is guaranteed to have a random char from all 4 character classes

        all_chars = string.ascii_letters + string.digits + string.punctuation
        password_chars += [secrets.choice(all_chars) for _ in range(length - 4)]
        secrets.SystemRandom().shuffle(password_chars)
        password = ''.join(password_chars)
        # Random letters, digits and symbols are added to fill the rest of the password past the intial 4 chars
        # The password is shuffled to prevent it starting predicatably with the same order of character classes at the start

        entropy = password_entropy_check(password)
        if entropy < 60:
            continue
        # The generated password is put through a function that finds the entropy in bits
        # If the entropy is less than 60 bits the loop continues and a new password is generated

        if password_commonpassword_check(password):
            continue
        # The generated password is put through a function that will check if password is in rockyou.txt
        # If the password is in rockyou.txt, the loop continues and a new pasword is generated

        if password_HIBP_check(password)[0]:  
            continue
        # The generated password is put through a function that will check if password is in HIBP
        # If the password is in HIBP, the loop continues and a new pasword is generated

        return password
        # Function ends and the password gets returned, if it passes all the tests