'''password_generator.py'''
'''This module provides a function to generate a random password with 20 digits length.'''
'''It includes functions to welcome the user, ask for the site name, generate a password, shuffle it, format it, check it for common words and save it to a text file.'''
'''This module is designed only for exercise purposes and does not include any "real" security features.'''


def load_common_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f if line.strip()]


def welcome():
    import time
    print("Welcome to the Password Generator!")
    time.sleep(2)
    print("This program will generate a random password for you and saved it to a text file.")
    time.sleep(2)


def ask_for_name():
    name = input(
        "Please enter for which site you want to generate a password:")
    return name


def generate_password():
    import random
    import string

    # Generate a random password of length 20 with unique characters
    part1 = random.choices(string.ascii_lowercase, k=5)
    part2 = random.choices(string.ascii_uppercase, k=5)
    part3 = random.choices(string.digits, k=5)
    part4 = random.choices(string.punctuation, k=5)

    password = part1 + part2 + part3 + part4
    random.shuffle(password)

    return ''.join(password[:20])


def format_password(password):
    # Format the password as 00000-00000-00000-00000
    return '-'.join([password[i:i+5] for i in range(0, 20, 5)])


def check_password_words(password):
    # Check if the password contains any common words
    commonen_words_list = load_common_words('common_words.txt')
    for word in commonen_words_list:
        if word in password.lower():
            return False
    return True


def save_password(name, password):
    # Save the password to a text file
    import os
    # data.txt is created if it does not exist
    if not os.path.exists('password.txt'):
        open('password.txt', 'a').close()
    try:
        with open('password.txt', 'a') as file:
            file.write(f"Site: {name}\n")
            file.write(f"Password: {password}\n")
    except IOError:
        print("Error opening file.")


def main():
    welcome()
    import time
    site_name = ask_for_name()
    while True:
        password = generate_password()
        formatted_password = format_password(password)
        if check_password_words(formatted_password):
            break
    save_password(site_name, formatted_password)
    print(f"Your password for {site_name} has been generated and saved.")
    time.sleep(3)


if __name__ == "__main__":
    main()
