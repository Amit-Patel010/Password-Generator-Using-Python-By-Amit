import string
import secrets

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))

def generate_passwords():
    num_passwords = int(input("How many passwords would you like to generate? "))
    passwords = []

    for i in range(num_passwords):
        length = int(input(f"Enter the length for password {i+1}: "))
        if length < 8:
            print("Password length should be at least 8. Using 8 characters as the default.")
            length = 8
        password = generate_password(length)
        passwords.append(password)

    print("\nGenerated passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")

def main():
    while True:
        generate_passwords()

        response = input("\nWanna generate more? (yes/no): ").strip().lower()
        if response != 'yes':
            print("Exiting the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main()