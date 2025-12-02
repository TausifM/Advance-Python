from fastapi import APIRouter
from models.user import User, UserResponse
from database.connection import db 
from bson import ObjectId

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create-user", response_model=UserResponse)
async def create_user(user: User):
    user_dict = user.model_dump()
    result = await db.users.insert_one(user_dict) 
    user_dict["_id"] = str(result.inserted_id)
    return UserResponse(**user_dict)

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