from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


# What we expect when someone REGISTERS
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.viewer  # default role is viewer


# What we expect when someone LOGS IN
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# What we RETURN about a user (never return password!)
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole

    class Config:
        from_attributes = True


# What we return after successful login
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse