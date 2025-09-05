from Create_Password import generate_secure_password

def secure_password_gen():
# Defines a function that generates a secure password by running an external function 
    input("Press Enter to generate a secure password...")

    password = generate_secure_password()
    print("\n🔒 Your new secure password is:\n")
    print(f"  {password}\n")
    print("Make sure to save it somewhere safe!\n")
    # Waits for user input to initiate password generation
    # Calls the external secure password generator function and prints the generated password

