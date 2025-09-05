from md5_crack import crack_md5_hashfile
from sha1_crack import crack_sha1_hashfile
from sha256_crack import crack_sha256_hashfile
from sha512_crack import crack_sha512_hashfile
from ntlm_crack import crack_ntlm_hashfile
from bcrypt_crack import crack_bcrypt_hashfile
from scrypt_crack import crack_scrypt_hashfile
from argon2_crack import crack_argon2_hashfile
from unknown_crack import crack_unknown_hashfile
from zipfile_crack import crack_zipfile
from rarfile_crack import crack_rarfile
from sevenzipfile_crack import crack_7zfile
from pdffile_crack import crack_pdf_file
from officefile_crack import crack_office_file
from find_hash_algorithms import detect_hash_algorithms

def password_cracker():
# Defining function that cracks the users password
    while True:
        print("\n=== Password Cracker ===")
        print("Enter 1 To Crack A Hashfile")
        print("Enter 2 To Crack A Password Protected File")
        print("Enter 3 To Discover Hashing Algorithms In Hash File")
        print("Enter 0 To Exit")
        # Password cracker main menu

        user_choice = input("Your choice: ")

        if user_choice == "1":
            print("\n=== Crack Hash File ===")
            print("Enter 1 To Crack A MD5 Hash File")
            print("Enter 2 To Crack A SHA-1 Hash File")
            print("Enter 3 To Crack A SHA-256 Hash File")
            print("Enter 4 To Crack A SHA-512 Hash File")
            print("Enter 5 To Crack A NTLM Hash File")
            print("Enter 6 To Crack A bcrypt Hash File")
            print("Enter 7 To Crack A scrypt Hash File")
            print("Enter 8 To Crack A argon2 Hash File")
            print("Enter 9 To Crack A Hash File Without Specifying Format (slower, not recommended)")
            # Hash file cracking submenu

            hash_file_choice = input("Your choice: ")

            if hash_file_choice == "1":
                crack_md5_hashfile()
            elif hash_file_choice == "2":
                crack_sha1_hashfile()
            elif hash_file_choice == "3":
                crack_sha256_hashfile()
            elif hash_file_choice == "4":
                crack_sha512_hashfile()
            elif hash_file_choice == "5":
                crack_ntlm_hashfile()
            elif hash_file_choice == "6":
                crack_bcrypt_hashfile()
            elif hash_file_choice == "7":
                crack_scrypt_hashfile()
            elif hash_file_choice == "8":
                crack_argon2_hashfile()
            elif hash_file_choice == "9":
                crack_unknown_hashfile()
            else:
                print("Invalid choice.")
            # Calls correct cracking function depending on the users selection

        elif user_choice == "2":
            print("\n=== Crack Password Protected File ===")
            print("Enter 1 To Crack A Password Protected ZIP File")
            print("Enter 2 To Crack A Password Protected RAR File")
            print("Enter 3 To Crack A Password Protected 7z File")
            print("Enter 4 To Crack A Password Protected PDF File")
            print("Enter 5 To Crack A Password Protected Office File")
            # Password protected file cracking submenu

            password_file_choice = input("Your choice: ")

            if password_file_choice == "1":
                crack_zipfile()
            elif password_file_choice == "2":
                crack_rarfile()
            elif password_file_choice == "3":
                crack_7zfile()
            elif password_file_choice == "4":
                crack_pdf_file()
            elif password_file_choice == "5":
                crack_office_file()
            else:
                print("Invalid choice.")
            # Calls correct cracking function depending on the users selection

        elif user_choice == "3":
            detect_hash_algorithms()
            # Calls function that detects hash algorithms in a file

        elif user_choice == "0":
            print("Exiting program. Goodbye!")
            break
            # Exits program

        else:
            print("Invalid choice. Please try again.\n")
            # Invalid menu input
        
        input("\nPress Enter to continue...")
        # Pause before continuing

        while True:
            again = input("Do you want to return to the password cracker menu? (y/n): ").strip().lower()
            if again == "y":
                break  
            elif again == "n":
                print("Exiting password cracker. Goodbye!")
                return  
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        # Ask user if they want to return to the main menu
