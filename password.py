import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
