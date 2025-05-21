import pytest
from src.users.api.schemas.registration_request import RegistrationRequest


def test_valid_registration_request():
    registration_request = RegistrationRequest(email="test@example.com", password="Password123!", confirm_password="Password123!")
    assert registration_request.email == "test@example.com"
    assert registration_request.password == "Password123!"
    assert registration_request.confirm_password == "Password123!"

def test_invalid_email():
    with pytest.raises(ValueError):
        RegistrationRequest(email="invalid-email", password="Password123!", confirm_password="Password123!")

def test_invalid_password():
    with pytest.raises(ValueError):
        RegistrationRequest(email="test@example.com", password="short", confirm_password="short")

def test_password_mismatch():
    with pytest.raises(ValueError):
        RegistrationRequest(email="test@example.com", password="Password123!", confirm_password="Password1234!")

