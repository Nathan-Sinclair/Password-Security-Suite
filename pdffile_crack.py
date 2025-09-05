import subprocess
import os

def crack_pdf_file():
# Defines a function that cracks password protected PDF files
    print("John The Ripper must be installed on your computer")
    print("Strawberry perl must be installed on your computer")
    print("During a brute-force attack, the time required depends on password complexity.")
    print("CTRL + C will close the program\n")
    # Informs the user about required dependencies and usage notes
    
    john_path = input("Enter the full path to your John the Ripper 'run' folder (where john.exe is): ").strip()
    pdf_file = input("Enter the full path to your password protected pdf file: ").strip()
    wordlist_file = input("Enter the full path to your wordlist file: ").strip()
    # Prompts user to enter the full paths to the John The Ripper folder, the password-protected PDF file and the wordlist

    if not os.path.isfile(pdf_file):
        print("PDF file not found. Exiting.")
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

    hash_file = pdf_file + ".hash"
    cleaned_hash_file = pdf_file + "_clean.hash"
    # Define filenames for the raw hash and cleaned hash outputs

    try:
        print("[*] Generating cleaned hash file...")
        pdf2john_pl = os.path.join(john_path, "pdf2john.pl")

        result = subprocess.run(
            ["perl", pdf2john_pl, pdf_file],
            capture_output=True,
            text=True,
            check=True
        )
        # Runs pdf2john to get hash output and captures it

        cleaned_lines = []
        for line in result.stdout.splitlines():
            if ":" in line:
                cleaned_lines.append(line.split(":", 1)[1])
        # Cleans the hash output

        with open(cleaned_hash_file, "w", encoding="ascii") as f:
            f.write("\n".join(cleaned_lines))
        # Save cleaned hash to file

    except subprocess.CalledProcessError:
        print("Error: Failed to generate hash file.")
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
                [os.path.join(john_path, "john")] + stage["args"] + [cleaned_hash_file],
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