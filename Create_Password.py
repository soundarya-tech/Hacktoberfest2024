import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the remaining length of the password with random choices from all sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Example usage
password_length = 12
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")
