from pydantic import BaseModel, EmailStr, Field
class User(BaseModel):
    name: str = Field(..., description="The full name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    password: str  = Field(..., description="The password for the user account") 
    phone: int = Field(..., description="The phone number of the user")

class UserResponse(User):
    id: str = Field(..., description="The unique identifier of the user", alias="_id")
    name: str  = Field(..., description="The full name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    phone: int = Field(..., description="The phone number of the user")

