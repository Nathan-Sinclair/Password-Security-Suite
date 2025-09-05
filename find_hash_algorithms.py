import os
import re

def detect_hash_algorithms():
# Defines a function that identifies the likely hashing algorithm used for each hash in a file
    
    hash_file = input("Enter the full path to your hash file: ").strip()
    if not os.path.isfile(hash_file):
        print("File not found. Exiting.")
        return
    # Prompts user to enter file path of hash file. If file path is invalid it will exit the function

    with open(hash_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Hash file is empty. Exiting.")
        return
    # Opens the hash file and stores in a list. Exits function if hash file is empty

    print("\n=== Hash Algorithm Detection ===")

    for idx, line in enumerate(lines, 1):
   
        hash_str = line.strip()
        if not hash_str:
            continue  

        algorithm = "Unknown"

        if re.match(r"^\$2[abxy]\$\d{2}\$[./A-Za-z0-9]{53}$", hash_str):
            algorithm = "bcrypt"

        elif re.match(r"^\$s0\$[a-z0-9]+\$[A-Za-z0-9+/=]+", hash_str):
            algorithm = "scrypt"

        elif re.match(r"^[A-F0-9]{32}$", hash_str):
            algorithm = "NTLM (MD4 based)"

        elif re.match(r"^[a-fA-F0-9]{32}$", hash_str):
            algorithm = "MD5"

        elif re.match(r"^[a-fA-F0-9]{40}$", hash_str):
            algorithm = "SHA-1"

        elif re.match(r"^[a-fA-F0-9]{64}$", hash_str):
            algorithm = "SHA-256"
            
        elif re.match(r"^[a-fA-F0-9]{128}$", hash_str):
            algorithm = "SHA-512"

        print(f"Line {idx}: {hash_str}")
        print(f"  Detected hash algorithm: {algorithm}\n")
        # Iterate through each hash in list
        # For each hash, check if it matches a known pattern to identify the hashing algorithm. Print the result.
