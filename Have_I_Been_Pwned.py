import hashlib
import requests 

def password_HIBP_check(password): 
# Defines a function that checks if the users password is not in the HIBP pwned passwords database

    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() 
    # Generate an uppercase SHA-1 hash of the users password (UTF-8 encoded) to match HIBP API format

    prefix, suffix = sha1_password[:5], sha1_password[5:]
    # Split the 40-character SHA-1 hash into a 5-character prefix and 35-character suffix for secure API querying

    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    # Sends a HTTP GET request to the HIBP API that returns the suffixes of all the hashed passwords that have the same prefix of user password

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from HIBP API: {response.status_code}")
        # If the server returns an unsuccessful response the code will close and print error message

    hashes = (line.split(':') for line in response.text.splitlines())
    # Parse the API response by splitting each line at ':' to create (hash_suffix, count) pairs

    for h, count in hashes:
    # This iterates through the hashes list
        if h == suffix:
            return True, int(count)  
            # During each loop if the suffix value from the API list is equal to the suffix of our password it will return True and the count as an integer
    return False, 0
    # If no passwords match the function will return False

