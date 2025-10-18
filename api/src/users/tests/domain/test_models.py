from uuid import UUID
import pytest

from src.users.domain.models import Email, User, Username

def test_valid_emails():
    valid_emails = [
        "test@example.com",
        "user.name+tag+sorting@example.com",
        "user_name@example.co.uk",
        "user-name@sub.example.org",
        "user123@domain123.com"
    ]

    for email in valid_emails:
        try:
            result = Email(email=email)
            assert result.email == email, f"Expected {email}, got {result.email}"
        except ValueError:
            pytest.fail(f"Valid email '{email}' raised ValueError unexpectedly.")
    
def test_invalid_emails():
    invalid_emails = [
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@com",
        "username@domain..com",
        "user..@example.com",
    ]

    for email in invalid_emails:
        with pytest.raises(ValueError, match=r"Invalid email format"):
            Email(email=email)

def test_valid_usernames():
    valid_usernames = [
        "user123",
        "user_name",
        "user.name",
        "user-name",
        "UserName",
        "u3r_n4m3"
    ]

    for username in valid_usernames:
        try:
            result = Username(username=username)
            assert result.username == username, f"Expected {username}, got {result.username}"
        except ValueError:
            pytest.fail(f"Valid username '{username}' raised ValueError unexpectedly.")

def test_invalid_usernames():
    invalid_usernames = [
        "ab",               # Too short
        "thisisaverylongusername",  # Too long
        "user name",       # Space not allowed
        "user@name",       # Special character not allowed
        "user!",           # Special character not allowed
        "user$name",       # Special character not allowed
    ]

    for username in invalid_usernames:
        with pytest.raises(ValueError, match=r"Invalid username format"):
            Username(username=username)

def test_user_creation():
    id = UUID("12345678-1234-5678-1234-567812345678")
    email = Email(email="mail@e.com")
    hashed_password = "hashed_password"
    username = Username(username="validUser")
    user = User(id=id, email=email, hashed_password=hashed_password, username=username)
    assert user.id == id, "User ID should be generated"
    assert user.email == email, "User email should match the provided email"
    assert user.hashed_password == hashed_password, "User hashed password should match the provided password"
    assert user.username == username, "User username should match the provided username"
    