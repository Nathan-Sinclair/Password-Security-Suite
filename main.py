import sys
from Password_Strength_Tester import passwordstrength_analyser
from Secure_Password_Generator import secure_password_gen
from Password_Crack import password_cracker

def main_menu():
# Defines the main menu function
    print(" ┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏━┓┏━╸┏━╸╻ ╻┏━┓╻╺┳╸╻ ╻   ┏━┓╻ ╻╻╺┳╸┏━╸   ╻ ╻ ╺┓ ")
    print(" ┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┗━┓┣╸ ┃  ┃ ┃┣┳┛┃ ┃ ┗┳┛   ┗━┓┃ ┃┃ ┃ ┣╸    ┃┏┛  ┃ ")
    print(" ╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ┗━┛┗━╸┗━╸┗━┛╹┗╸╹ ╹  ╹    ┗━┛┗━┛╹ ╹ ┗━╸   ┗┛ ╹╺┻╸")
    print(" ┏┓ ╻ ╻   ┏┓╻┏━┓╺┳╸╻ ╻┏━┓┏┓╻   ┏━┓╻┏┓╻┏━╸╻  ┏━┓╻┏━┓ ")
    print(" ┣┻┓┗┳┛   ┃┗┫┣━┫ ┃ ┣━┫┣━┫┃┗┫   ┗━┓┃┃┗┫┃  ┃  ┣━┫┃┣┳┛ ")
    print(" ┗━┛ ╹    ╹ ╹╹ ╹ ╹ ╹ ╹╹ ╹╹ ╹   ┗━┛╹╹ ╹┗━╸┗━╸╹ ╹╹╹┗╸ ")
    # Displays an ASCII banner for styling
    while True:
        print("\nEnter 1 For Password Strength Analyser")
        print("Enter 2 For Secure Password Generator")
        print("Enter 3 For Password Cracker")
        print("Enter 0 To Exit")
        # Continuously prompts the user to choose an option
        user_choice = input("Your choice: ")

        if user_choice == "0":
            print("Exiting program. Goodbye!")
            sys.exit()
        elif user_choice == "1":
            passwordstrength_analyser()
        elif user_choice == "2":
            secure_password_gen()
        elif user_choice == "3":
            password_cracker()
        else:
            print("Invalid choice. Please try again.\n")
        # Calls the appropriate function based on the user's choice
        # Exits the program cleanly when the user selects 0
if __name__ == "__main__": 
    main_menu()