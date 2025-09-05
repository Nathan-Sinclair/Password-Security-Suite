from Password_Length import password_length_check
from Character_Class_Counting import password_characterclass_check
from Entropy_Calculation import password_entropy_check
from Common_Passwords import password_commonpassword_check
from Have_I_Been_Pwned import password_HIBP_check
from Password_Strength import password_strength_check
import pwinput # type: ignore

def passwordstrength_analyser():
# Defines a function that evaluates a user's password by running external checks and determining its strength
    while True:
        choice = input("Do you want your password to be hidden while typing? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.\n")

    if choice == 'y':
        password = pwinput.pwinput("\nEnter your password: ")
    else:
        password = input("\nEnter your password: ")
    # Prompts the user to enter their password and stores their input, giving option to hiding it as they type

    length_of_password = password_length_check(password)
    number_of_character_classes = password_characterclass_check(password)
    entropy_score = password_entropy_check(password)
    rockyou_check = password_commonpassword_check(password)
    HIBP_check = password_HIBP_check(password)[0]
    # Calls external functions to gather key data of the password

    password_rating = password_strength_check(
        length_of_password,
        number_of_character_classes,
        entropy_score,
        rockyou_check,
        HIBP_check
    )
    # Calls the password_strength_check function with the gathered password data as arguments

    if password_rating == "Strong":
        print("\n✅ Excellent! Your password is rated strong. It meets all recommended security standards.")
    
    elif password_rating == "Moderate":
        print("\n⚠️ Your password is moderate. It's decent, but consider strengthening it for better protection.\n")
        print("🔧 Suggestions to improve:\n")
        if 8 <= length_of_password <= 11:
            print("- Increase the password length to more than 12 characters.")
        if number_of_character_classes < 4:
            print("- Use a mix of uppercase, lowercase, numbers, and symbols.")
        if entropy_score < 60:
            print("- Use more unpredictable combinations to increase entropy.")
            
    else: 
        print("\n❌ Warning: Your password is weak. It does not meet basic security criteria. Please consider creating a stronger one.\n")
        print("🔧 Suggestions to improve:\n")
        if length_of_password < 12:
            print("- Increase the password length to more than 12 characters.")
        if number_of_character_classes < 4:
            print("- Use a mix of uppercase, lowercase, numbers, and symbols.")
        if entropy_score < 60:
            print("- Use more unpredictable combinations to increase entropy.")
        if HIBP_check:
            print("- Your password has appeared in known data breaches (HaveIBeenPwned). It is strongly recommended to change it.")
        if rockyou_check:
            print("- Your password was found in the RockYou.txt common password list. Consider choosing a more unique password.")
    # Prints the password rating and suggests improvements to increase strength

    input("\nPress Enter to exit...")
    return password_rating
