VERSION = "0.1.0"


def greet(name):
    return f"Hello, {name}!"

def get_user_input():
    return input("Enter your name: ")


def add(a, b):
    return a + b


def validate_email(email):
    return "@" in email


if __name__ == "__main__":
    name = get_user_input()
    print(greet(name))