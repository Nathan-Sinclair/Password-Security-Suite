import subprocess
import os

def crack_office_file():
# Defines a function that cracks password protected office files
    print("John The Ripper must be installed on your computer")
    print("Python 3.8+ must be installed on your computer (to run office2john.py)")
    print("During a brute-force attack, the time required depends on password complexity.")
    print("CTRL + C will close the program\n")
    # Informs the user about required dependencies and usage notes
    
    john_path = input("Enter the full path to your John the Ripper 'run' folder (where john.exe is): ").strip()
    office_file = input("Enter the full path to your password protected Office file: ").strip()
    wordlist_file = input("Enter the full path to your wordlist file: ").strip()
    # Prompts user to enter the full paths to the John The Ripper folder, the password-protected office file and the wordlist

    if not os.path.isfile(office_file):
        print("Office file not found. Exiting.")
        return
    if not os.path.isfile(wordlist_file):
        print("Wordlist file not found. Exiting.")
        return
    if not os.path.isdir(john_path):
        print("John run folder not found. Exiting.")
        return
    # Check if paths user provided exist, if a path doesnt exist it exits the function


    pot_file = os.path.join(john_path, "john.pot")
    if os.path.exists(pot_file):
        os.remove(pot_file)
    # Deletes existing pot file to start with a clean slate each time

    hash_file = office_file + ".hash"
    # Define filenames for the raw hash 

    try:
        print("[*] Generating hash file from Office file...")
        office2john_py = os.path.join(john_path, "office2john.py")
        with open(hash_file, "w", encoding="ascii") as f:
            subprocess.run(
                ["py", "-3.8", office2john_py, office_file],
                stdout=f,
                check=True,
                text=True
            )
        # Runs office2john to get hash output and captures it

    except subprocess.CalledProcessError:
        print("Error: Failed to generate hash file from Office file.")
        return
    # Exits function if hash generation fails

    stages = [
        {"desc": "Wordlist attack", "args": [f"--wordlist={wordlist_file}"]},
        {"desc": "Wordlist + mutations (rules)", "args": [f"--wordlist={wordlist_file}", "--rules"]},
        {"desc": "Brute force attack", "args": ["--incremental"]}
    ]
    # Define cracking stages for John the Ripper

    for stage in stages:
        print(f"\n=== Starting: {stage['desc']} ===")
        try:
            subprocess.run(
                [os.path.join(john_path, "john")] + stage["args"] + [hash_file],
                check=True
            )
        except FileNotFoundError:
            print("John the Ripper executable not found. Make sure 'john.exe' exists in the run folder.")
            return
        except subprocess.CalledProcessError:
            print(f"Error running John in stage: {stage['desc']}")
    # Run each cracking stage and handle errors

    print("\n=== Cracked Passwords ===")
    if os.path.exists(pot_file):
        with open(pot_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        passwords = []
        for line in lines:
            if ":" in line:
                parts = line.strip().split(":")
                if len(parts) > 1:
                    password = parts[-1].split()[0]
                    passwords.append(password)

        if passwords:
            for pw in passwords:
                print(f" - {pw}")
        else:
            print("No passwords found in pot file.")
    else:
        print("Pot file not found. No passwords were cracked.")
    # Read the pot file and display cracked passwords; if none are found user is notified 
