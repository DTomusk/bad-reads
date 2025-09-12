import re
from pydantic import BaseModel, field_validator

class RegistrationRequest(BaseModel):
    email: str
    password: str
    confirm_password: str
    username: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email address')
        return v
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', v):
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one number, and one special character')
        return v
    
    @field_validator('confirm_password')
    @classmethod
    def validate_confirm_password(cls, v, info):
        if 'password' not in info.data:
            raise ValueError('Password is required')
        if v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v
    
    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_.-]{3,20}$', v):
            raise ValueError('Username must be 3-20 characters long and can only contain letters, numbers, underscores, hyphens, and periods')
        return v
    
    
    
    

