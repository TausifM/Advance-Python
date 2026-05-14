from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials
from models.user import User, UserResponse, LoginRequest
from database.connection import db
from bson import ObjectId
from utils.hash import hash_password, verify_password
from middleware.auth import auth_middleware, security, create_access_token

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create-user")
async def create_user(user: User):

    user_dict = user.model_dump()

    existing_user = await db.users.find_one({
        "email": user_dict["email"]
    })

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )

    # HASH PASSWORD
    user_dict["password"] = hash_password(
        user_dict["password"]
    )

    result = await db.users.insert_one(user_dict)

    user_dict["_id"] = str(result.inserted_id)

    # CREATE JWT TOKEN
    token = create_access_token({
        "id": user_dict["_id"],
        "email": user_dict["email"]
    })

    return {
        "success": True,
        "message": "User created successfully",
        "token": token,
        "user": UserResponse(**user_dict)
    }

@router.post("/login")
async def login_user(login_request: LoginRequest):

    user = await db.users.find_one({
        "email": login_request.email
    })

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(
        login_request.password,
        user["password"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    user["_id"] = str(user["_id"])

    # CREATE JWT TOKEN
    token = create_access_token({
        "id": user["_id"],
        "email": user["email"]
    })

    return {
        "success": True,
        "token": token,
        "user": UserResponse(**user)
    }

# PROTECTED ROUTE
@router.put(
    "/update-user/{user_id}",
    response_model=UserResponse
)
async def update_user(
    user_id: str,
    user: User,
    request: Request,
    current_user=Depends(auth_middleware)
):

    user_dict = user.model_dump()

    await db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": user_dict}
    )

    updated_user = await db.users.find_one({
        "_id": ObjectId(user_id)
    })

    updated_user["_id"] = str(updated_user["_id"])

    return UserResponse(**updated_user)

# PROTECTED ROUTE
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user(
    user_id: str,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    current_user=Depends(auth_middleware)
):
    user = await db.users.find_one({
        "_id": ObjectId(user_id)
    })

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user["_id"] = str(user["_id"])

    return UserResponse(**user)


# PROTECTED ROUTE
@router.delete("/delete-user/{user_id}")
async def delete_user(
    user_id: str,
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    current_user=Depends(auth_middleware)
):
    result = await db.users.delete_one({
        "_id": ObjectId(user_id)
    })

    if not result.deleted_count:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "success": True,
        "message": "User deleted successfully"
    }