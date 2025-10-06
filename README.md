# Password Security Suite
## Purpose:
Allows users to generate secure passwords, analyse their strength, and test their resilience.

## What Is It:
A toolkit consisting of three tools:

1. **Password Strength Analyser** – Evaluates the user's entered password and provides a strength rating of strong, moderate, or weak.
2. **Secure Password Generator** – Generates a strong, random password that meets the recommended security criteria.
3. **Password Cracker** – Cracks passwords from password-protected files or hash files.
   
These tools have been created in the Python programming language.

## Features:
### Main Menu:
- Displays a styled ASCII banner for visual appeal.
- Simple, interactive text-based navigation.
- Lets users choose between:
  - Password Strength Analyser.
  - Secure Password Generator.
  - Password Cracker.
- Interactive menu with clear results and easy return/exit options.
- Handles invalid input gracefully with error messages.

### Password Strength Analyser
- Allows user to enter passwords masked or visible.
- Checks password length, character complexity, entropy, and whether it appears in the RockYou password list or data breaches (HaveIBeenPwned).
- Rates passwords as strong, moderate, or weak.
- Suggests improvements for weak or moderate passwords.
- Clear, emoji-enhanced feedback (✅ ⚠️ ❌).
- Handles invalid input gracefully with error messages.

### Secure Password Generator
- Generates secure, strong, random passwords.
- Ensures character complexity.
- Shuffles characters to prevent predictable patterns.
- Checks entropy and rejects weak passwords.
- Avoids common passwords (RockYou) and breached passwords (HaveIBeenPwned).
- Simple, user-friendly output.

### Password Cracker
- Cracks various hash types (MD5, SHA-1, SHA-256, SHA-512, NTLM, bcrypt, scrypt, Argon2).
- Cracks unknown hash types.
- Cracks password-protected files (ZIP, RAR, 7z, PDF, Office).
- Detects hash algorithms in hash files.
- Interactive menu with clear results and easy return/exit options.
- Handles invalid input gracefully with error messages.

## Prerequisites & Dependencies:
### Python 
- Install Python version 3.8.10: https://www.python.org/downloads/
- Python version 3.8.10 is needed specifically to run the script to crack Office files 
- Add Python to your system PATH during installation. Folder containing python.exe needs to be listed in PATH. By default it is usually something like this C:\Python38\
- Install requests library. Type "pip install requests" in terminal to install.
- Install pwinput library. Type "pip install pwinput" in terminal to install.
### Strawberry Perl
- Install Strawberry Perl: https://strawberryperl.com/
- Make sure it is added to your system PATH. Perl.exe is in the bin folder. By default it is usually something like this C:\Strawberry\perl\bin
### John The Ripper Jumbo
- Download the Jumbo version from Openwall: https://www.openwall.com/john/
- Ensure the executable (john.exe) is accessible via PATH. By default it is usually something like this C:\John\run
### Wordlist
- rockyou.txt is too large to be included in the GitHub repository. Please download rockyou.txt separately and save it in the repository folder on your local machine with the filename "rockyou.txt".
- If you want to use a different wordlist, save it in the repository folder and name it "rockyou.txt" so the program can access it correctly.
- Install rockyou.txt from this link https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt 

## Installation Instructions:
1. Install prerequisites and dependencies.
2. Clone or download the repository folder to your local machine.
3. Open a terminal and navigate to the repository folder.
4. Run the main program. Type "python main.py".
5. Follow the on-screen prompts to use; Password Strength Analyser, Secure Password Generator & Password Cracker.
### Run With Docker:
You can run the Password Security Suite in a Docker container, which includes John the Ripper, Python 3.8, and required dependencies.
- Make sure the `Dockerfile` is located in the `docker/` folder at the repository root. Then build the image:

  docker build -t password-security-suite -f docker/Dockerfile .

- Start the container interactively (with wordlist mount):

  docker run -it -v /absolute/path/to/your/wordlists:/app/wordlists password-security-suite

- Once inside the container, navigate to the app folder (if needed) and run:

  python main.py

- To use a local wordlist like `rockyou.txt`, mount the folder into the container:

  docker run -it -v /path/to/wordlists:/app/wordlists password-security-suite
  
## Troubleshooting:
- python is not recognized as an internal or external command. Cause & Fix: Python is not installed or not in PATH, add it to your PATH.
- john is not recognized or FileNotFoundError: john.exe not found. Cause & Fix: John The Ripper is not installed or not in PATH, add it to your PATH.
- Hash file is not formatted correctly for John The Ripper to read. Cause & Fix: To format the hash file correctly refer to John’s README: https://www.openwall.com/john/doc/README.shtml
- John The Ripper cannot read the hash file. Cause & Fix: Some hash files are saved with a BOM (Byte Order Mark), which John cannot process. Save the file without BOM encoding.
- perl is not recognized when cracking PDF or 7z files. Cause & Fix: Strawberry Perl is not installed or not in PATH, add it to your PATH.
- Python does not work when cracking Office files. Cause & Fix: Python 3.8.10 is not installed or not in PATH, add it to your PATH.
- Wordlist file not found. Cause & Fix: The program cannot locate rockyou.txt. Make sure rockyou.txt is included in the repository folder, or provide the full path manually when asked.
- No passwords found in pot file. Cause: The password could not be cracked with the provided wordlist and attack methods.
- Hash detection shows unknown. Cause & Fix: The hash doesn’t match common patterns (MD5, SHA-1, SHA-256, SHA-512, NTLM, bcrypt, scrypt, argon2).

## Screenshot:
<img width="704" height="244" alt="image" src="https://github.com/user-attachments/assets/1e45bf6b-fe75-4da1-8f40-419c489cfceb" />

## Credits:
### Tools
- John The Ripper: password cracking tool.

### Wordlists & Data Sources
- rockyou.txt: Common password list used for testing and password cracking.
- HaveIBeenPwned: API, breached passwords.
  
### Contributors 
- Nathan Sinclair: sole developer of the project (design, coding, and documentation).

### AI Tools
- ChatGPT & Copilot – for code suggestions, explanations and debugging support.

### Special Thanks
- Stack Overflow: community Q&A, troubleshooting and solutions.


