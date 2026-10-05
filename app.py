
VERSION = "1.0.0"

import re


def greet(name):
    return f"Hello, {name.capitalize()}"

def get_user_input():
    return input("Enter your name: ")


def add(a, b):
    return a + b


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


if __name__ == "__main__":
    name = get_user_input()
    print(greet(name))