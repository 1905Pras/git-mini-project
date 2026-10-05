VERSION = "0.1.0"


def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def validate_email(email):
    return "@" in email


if __name__ == "__main__":
    print(greet("World"))