import random
import string

def generate_password(password_length):
    """
    Generates a secure random password of the specified length.
    Ensures at least one uppercase, one lowercase, one digit, and one symbol.
    """
    if password_length < 4:
        return "❌ Password length should be at least 4 characters for better security."


    all_characters = string.ascii_letters + string.digits + string.punctuation

    password_chars = [
        random.choice(string.ascii_uppercase),   
        random.choice(string.ascii_lowercase),   
        random.choice(string.digits),            
        random.choice(string.punctuation)        
    ]

    remaining_length = password_length - 4
    password_chars += random.choices(all_characters, k=remaining_length)

    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    print("🔐 Welcome to the Password Generator!")

    try:
        user_input = input("Enter the desired password length: ")
        password_length = int(user_input)

        generated_password = generate_password(password_length)
        print(f"\n🔑 Your generated password: {generated_password}")
    except ValueError:
        print("❌ Please enter a valid number (e.g., 8, 12, 16).")

if __name__ == "__main__":
    main()
