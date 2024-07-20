import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_punctuation=True):
    characters = string.ascii_lowercase  # Always include lowercase letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("No character types selected for password generation.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (yes/no, default is yes): ").lower() in ['yes', 'y']
        use_digits = input("Include digits? (yes/no, default is yes): ").lower() in ['yes', 'y']
        use_punctuation = input("Include punctuation? (yes/no, default is yes): ").lower() in ['yes', 'y']

        password = generate_password(length, use_uppercase, use_digits, use_punctuation)
        print(f"Generated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
