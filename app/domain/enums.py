"""Domain enums for the reservation system."""

from enum import Enum


class UserType(str, Enum):
    """Type of user in the system."""
    
    INTERNAL = "internal"
    EXTERNAL = "external"


class UserRole(str, Enum):
    """Role of user in the system."""
    
    MEMBER = "member"
    TECHNICIAN = "technician"
    MANAGER = "manager"
