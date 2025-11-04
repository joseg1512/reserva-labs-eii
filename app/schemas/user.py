"""User Pydantic schemas for request/response validation."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from app.domain.enums import UserRole, UserType

from uuid import UUID

class UserBase(BaseModel):
    """Base user schema with common attributes."""
    
    email: EmailStr
    user_type: UserType
    role: UserRole = UserRole.MEMBER
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a new user."""
    
    password: str = Field(..., min_length=8, description="User password (min 8 characters)")


class UserUpdate(BaseModel):
    """Schema for updating user information."""
    
    email: EmailStr | None = None
    user_type: UserType | None = None
    role: UserRole | None = None
    is_active: bool | None = None


class UserInDB(UserBase):
    """Schema for user as stored in database."""
    
    id: UUID
    password_hash: str
    is_active: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserBase):
    """Schema for user in API responses (excludes sensitive data)."""
    
    id: UUID
    is_active: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
