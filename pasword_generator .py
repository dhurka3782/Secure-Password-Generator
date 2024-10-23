import random
import string

def ask_user_preferences():
    """Ask the user for password requirements."""
    length = int(input("Enter the password length (minimum 8): "))
    if length < 8:
        print("Password length should be at least 8 for security. Setting to 8.")
        length = 8
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        print("At least one character type must be selected. Defaulting to all.")
        use_uppercase = use_lowercase = use_digits = use_special = True
    
    return length, use_uppercase, use_lowercase, use_digits, use_special

def generate_secure_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    """Generate a secure password with at least one character from each selected character set."""
    char_pool = ''
    mandatory_chars = []

    if use_uppercase:
        char_pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_pool += string.ascii_lowercase
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        mandatory_chars.append(random.choice(string.punctuation))

    if not char_pool:
        raise ValueError("No character sets selected.")

    # Fill the rest of the password with random characters from the full pool
    password = mandatory_chars + [random.choice(char_pool) for _ in range(length - len(mandatory_chars))]

    # Shuffle the password list to randomize the order of mandatory characters
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Main function to run the password generator
def main():
    print("Welcome to the Secure Password Generator!")
    
    # Ask the user for preferences
    length, use_uppercase, use_lowercase, use_digits, use_special = ask_user_preferences()
    
    # Generate the password based on user preferences
    password = generate_secure_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    
    print(f"Your secure password is: {password}")

if __name__ == "__main__":
    main()
