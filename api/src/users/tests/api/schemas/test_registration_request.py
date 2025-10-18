import pytest
from src.users.api.schemas.registration_request import RegistrationRequest


def test_valid_registration_request():
    registration_request = RegistrationRequest(email="test@example.com", password="Password123!", confirm_password="Password123!", username="Username")
    assert registration_request.email == "test@example.com"
    assert registration_request.password == "Password123!"
    assert registration_request.confirm_password == "Password123!"
    assert registration_request.username == "Username"

def test_invalid_email():
    with pytest.raises(ValueError):
        RegistrationRequest(email="invalid-email", password="Password123!", confirm_password="Password123!", username="Username")

def test_invalid_password():
    with pytest.raises(ValueError):
        RegistrationRequest(email="test@example.com", password="short", confirm_password="short", username="Username")

def test_password_mismatch():
    with pytest.raises(ValueError):
        RegistrationRequest(email="test@example.com", password="Password123!", confirm_password="Password1234!", username="Username")

@pytest.mark.parametrize("username", [
    "",            # empty
    "ab",          # too short
    "thisiswaytoolongforausername",  # too long
    "invalid space", # contains space
    "inv@lid!",     # contains special characters
])
def test_invalid_username(username):
    with pytest.raises(ValueError):
        RegistrationRequest(
            email="test@example.com",
            password="Password123!",
            confirm_password="Password123!",
            username=username,
        )

