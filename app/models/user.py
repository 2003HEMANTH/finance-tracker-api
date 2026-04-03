from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum


# Define the allowed roles as an Enum
class UserRole(str, enum.Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # User's full name
    name = Column(String, nullable=False)

    # Must be unique — used for login
    email = Column(String, unique=True, index=True, nullable=False)

    # Stored as a hashed string — never plain text
    hashed_password = Column(String, nullable=False)

    # Role controls what the user can access
    role = Column(Enum(UserRole), default=UserRole.viewer, nullable=False)