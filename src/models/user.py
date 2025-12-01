from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str 
    email: EmailStr
    password: str 
    phone: int

class UserResponse(User):
    id: str
    name: str
    email: EmailStr
    phone: int

