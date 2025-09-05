def password_strength_check(length, char_classes, entropy, common_password_found, hibp_found):
# Defines a function to determine the strength of a password
# This function takes five arguments, which are the five criteria used to measure the user's password strength
    if (length >= 12 and char_classes == 4 and entropy >= 60 and not common_password_found and not hibp_found):
        return "Strong"

    if (length >= 8 and char_classes >= 3 and entropy >= 36 and not common_password_found and not hibp_found):
        return "Moderate"
    
    return "Weak"
    # It evaluates each criterion and returns whether the password is weak, moderate, or strong
