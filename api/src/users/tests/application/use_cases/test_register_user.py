from uuid import uuid4
import pytest
from unittest.mock import MagicMock
from api.src.users.application.commands.register_user import RegisterUser
from src.users.domain.models import Email, User

@pytest.fixture
def mock_user_repository():
    """Fixture for a mocked UserRepository."""
    mock_repo = MagicMock()
    mock_repo.get_by_email.return_value = None
    mock_repo.get_by_username.return_value = None
    mock_repo.save = MagicMock()
    return mock_repo

@pytest.fixture
def mock_hasher():
    """Fixture for a mocked Hasher."""
    mock_hasher = MagicMock()
    mock_hasher.hash.return_value = "hashed_password"
    return mock_hasher

@pytest.fixture
def mock_profanity_service():
    """Fixture for a mocked profanity service"""
    mock_profanity_service = MagicMock()
    mock_profanity_service.string_contains_profanity.return_value = False
    return mock_profanity_service

@pytest.fixture
def register_user(mock_user_repository, mock_hasher, mock_profanity_service):
    """Fixture for the RegisterUser use case."""
    return RegisterUser(user_repository=mock_user_repository, hasher=mock_hasher, profanity_service=mock_profanity_service)

def test_register_user_success(register_user, mock_user_repository, mock_hasher, mock_profanity_service):
    # Arrange
    email = "test@example.com"
    password = "securepassword"
    username = "validUser"

    # Act
    outcome = register_user.execute(email=email, password=password, username=username)

    # Assert
    assert outcome is not None
    assert outcome.isSuccess is True
    assert outcome.data.id is not None, "User ID should be generated"
    assert outcome.data.email.email == email, "User email should match the provided email"
    assert outcome.data.hashed_password is not None, "User hashed password should be set"
    assert outcome.data.username
    mock_user_repository.get_by_email.assert_called_once_with(email)
    mock_user_repository.get_by_username.assert_called_once_with(username)
    mock_user_repository.save.assert_called_once_with(outcome.data)
    mock_hasher.hash.assert_called_once_with(password)
    mock_profanity_service.string_contains_profanity.called_once_with(username)
    mock_profanity_service.string_contains_profanity.called_once_with(email)


def test_register_user_existing_email(register_user, mock_user_repository, mock_hasher, mock_profanity_service):
    # Arrange
    mock_user_repository.get_by_email.return_value = User(
        id=uuid4(), email=Email(email="test@example.com"), hashed_password="hashed_password", username="validUser"
    )
    email = "test@example.com"
    password = "securepassword"
    username = "validUser"

    # Act
    outcome = register_user.execute(email=email, password=password, username=username)

    # Assert 
    assert outcome is not None
    assert outcome.isSuccess is not True
    assert outcome.failure is not None
    assert outcome.failure.error == "Email already in use."
    mock_user_repository.get_by_email.assert_called_once_with(email)
    mock_user_repository.get_by_username.assert_not_called()
    mock_user_repository.save.assert_not_called()
    mock_hasher.hash.assert_not_called()
    mock_profanity_service.string_contains_profanity.called_once_with(email)
    mock_profanity_service.string_contains_profanity.called_once_with(username)

def test_register_user_invalid_email(register_user, mock_user_repository, mock_hasher):
    # Arrange
    email = "invalid-email"
    password = "securepassword"
    username = "validUser"

    # Act
    outcome = register_user.execute(email=email, password=password, username=username)

    # Assert
    assert outcome is not None
    assert outcome.isSuccess is not True
    assert outcome.failure is not None
    assert outcome.failure.error == "Invalid email format: invalid-email"
    mock_user_repository.get_by_email.assert_not_called()
    mock_user_repository.save.assert_not_called()
    mock_hasher.hash.assert_not_called()

def test_register_user_existing_username(register_user, mock_user_repository, mock_hasher, mock_profanity_service):
    # Arrange
    mock_user_repository.get_by_username.return_value = User(
        id=uuid4(), email=Email(email="test@example.com"), hashed_password="hashed_password", username="validUser"
    )
    email = "test@example.com"
    password = "securepassword"
    username = "validUser"

    # Act
    outcome = register_user.execute(email=email, password=password, username=username)

    # Assert 
    assert outcome is not None
    assert outcome.isSuccess is not True
    assert outcome.failure is not None
    assert outcome.failure.error == "Username already in use."
    mock_user_repository.get_by_username.assert_called_once_with(username)
    mock_user_repository.save.assert_not_called()
    mock_hasher.hash.assert_not_called()
    mock_profanity_service.string_contains_profanity.called_once_with(email)
    mock_profanity_service.string_contains_profanity.called_once_with(username)

def test_register_user_invalid_username(register_user, mock_user_repository, mock_hasher):
    # Arrange
    email = "test@example.com"
    password = "securepassword"
    username = "ab"

    # Act
    outcome = register_user.execute(email=email, password=password, username=username)

    # Assert
    assert outcome is not None
    assert outcome.isSuccess is not True
    assert outcome.failure is not None
    assert outcome.failure.error == "Invalid username format: ab"
    mock_user_repository.get_by_username.assert_not_called()
    mock_user_repository.save.assert_not_called()
    mock_hasher.hash.assert_not_called()