from api.users.api.schemas.registration_request import RegistrationRequest


def test_valid_registration_request():
    registration_request = RegistrationRequest(email="test@example.com", password="Password123!", confirm_password="Password123!")
    assert registration_request.email == "test@example.com"
    assert registration_request.password == "Password123!"
    assert registration_request.confirm_password == "Password123!"
