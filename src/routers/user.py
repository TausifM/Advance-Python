from fastapi import APIRouter, HTTPException, status
from models.user import User, UserResponse, LoginRequest
from database.connection import db 
from bson import ObjectId
from utils.hash import hash_password, verify_password

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create-user", response_model=UserResponse)
async def create_user(user: User):
    user_dict = user.model_dump()
    if user_dict is None:
      raise ValueError("user_dict cannot be None")
    print(user_dict["password"])
    exiting_user = await db.users.find_one({"email": user_dict["email"]})
    if exiting_user and user_dict.get('email'):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
            )
    user_dict["password"] = hash_password(user_dict["password"])
    result = await db.users.insert_one(user_dict) 
    user_dict["_id"] = str(result.inserted_id)
    return UserResponse(**user_dict)

@router.post("/login")
async def login_user(login_request: LoginRequest):
    user = await db.users.find_one({"email": login_request.email})
    if user and verify_password(login_request.password, user["password"]):
        user["_id"] = str(user["_id"])
        return UserResponse(**user)
    return {"error": "Invalid email or password"}

@router.put('/update-user/{user_id}', response_model=UserResponse)
async def update_user(user_id: str, user: User):
    user_dict = user.model_dump()
    await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user_dict}) 
    user_dict["_id"] = user_id
    return UserResponse(**user_dict)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)}) 
    if user:
        user["_id"] = str(user["_id"])
        return UserResponse(**user)
    return {"error": "User not found"}

@router.delete("/delete-user/{user_id}")
async def delete_user(user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return {"message": "User deleted successfully"}
    return {"error": "User not found"}