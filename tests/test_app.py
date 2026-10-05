from app import greet, add, validate_email

#CI test
def test_greet():
    assert greet("Prasanth") == "Hello, Prasanth!"

def test_greet_capitalizes_name():
    assert greet("prasanth") == "Hello, Prasanth!"


def test_add():
    assert add(2, 3) == 5


def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("testexample.com") is False