import random
import sys
import itertools
import math
import os

# Character sets
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
lower_letters = [
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
    "a", "s", "d", "f", "g", "h", "j", "k", "l",
    "z", "x", "c", "v", "b", "n", "m"
]
upper_letters = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
    "A", "S", "D", "F", "G", "H", "J", "K", "L",
    "Z", "X", "C", "V", "B", "N", "M"
]
symbols = [
    "`", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/",
    "{", "}", "|", ":", "\"", "<", ">", "?", "~", "!",
    "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"
]

# Get the absolute path of the script
script_location = os.path.abspath(__file__)

# Print the script's location
print(f"Script is stored at: {script_location}")

# Function to generate a password
def generate_password(length=12, char_set="all"):
    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Select the character set
    if char_set == "numbers":
        characters = numbers
    elif char_set == "letters":
        characters = lower_letters + upper_letters
    elif char_set == "uppercase":
        characters = upper_letters
    elif char_set == "all":
        characters = numbers + lower_letters + upper_letters + symbols
    else:
        print("Invalid character set. Choose from: numbers, letters, uppercase, all.")
        return None

    # Generate the password
    password = ''.join(random.choices(characters, k=length))
    return password

# Function to test password strength
def password_strength(password):
    char_space = 0
    if any(char in numbers for char in password):
        char_space += len(numbers)
    if any(char in lower_letters for char in password):
        char_space += len(lower_letters)
    if any(char in upper_letters for char in password):
        char_space += len(upper_letters)
    if any(char in symbols for char in password):
        char_space += len(symbols)
    
    # Estimate cracking time (brute-force)
    combinations = math.pow(char_space, len(password))
    crack_time_seconds = combinations / 1_000_000_000  # Assuming 1 billion guesses/sec
    return crack_time_seconds

# Function to check if a password is in rockyou.txt
def is_in_rockyou(password, file_path="C:/PATH/$/commands/system/pwgen/rockyou.txt"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return False

    with open(file_path, "r", encoding="latin-1") as f:
        for line in f:
            if password == line.strip():
                return True
    return False

# Wizard Mode
def wizard_mode():
    print("Welcome to the Password Generator Wizard!")
    length = int(input("Enter the desired password length (min 4): "))
    print("Choose the character set:")
    print("1. Numbers only")
    print("2. Letters only")
    print("3. Uppercase only")
    print("4. All characters")
    choice = int(input("Enter your choice (1-4): "))
    char_set = {1: "numbers", 2: "letters", 3: "uppercase", 4: "all"}.get(choice, "all")
    
    password = generate_password(length, char_set)
    if password:
        print(f"Generated password: {password}")
        strength = password_strength(password)
        print(f"Estimated cracking time: {strength:.2f} seconds ({strength/3600:.2f} hours).")
        print("Checking if the password exists in rockyou.txt...")
        if is_in_rockyou(password):
            print("Warning: This password exists in the rockyou.txt dictionary and is not secure!")
        else:
            print("This password is not in the rockyou.txt dictionary and is more secure.")

# Main logic
if __name__ == "__main__":
    if len(sys.argv) == 1:
        wizard_mode()
    else:
        import argparse
        parser = argparse.ArgumentParser(description="Advanced Password Generator")
        parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
        parser.add_argument("-c", "--charset", type=str, choices=["numbers", "letters", "uppercase", "all"],
                            default="all", help="Character set for password")
        parser.add_argument("-t", "--test", type=str, help="Test the strength of a given password")
        parser.add_argument("-r", "--rockyou", type=str, help="Check if a password exists in rockyou.txt")

        args = parser.parse_args()

        if args.test:
            strength = password_strength(args.test)
            print(f"Estimated cracking time: {strength:.2f} seconds ({strength/3600:.2f} hours).")
        elif args.rockyou:
            if is_in_rockyou(args.rockyou):
                print("Warning: This password exists in the rockyou.txt dictionary and is not secure!")
            else:
                print("This password is not in the rockyou.txt dictionary and is more secure.")
        else:
            password = generate_password(args.length, args.charset)
            if password:
                print(f"Generated password: {password}")
