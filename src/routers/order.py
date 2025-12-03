from fastapi import APIRouter, HTTPException, status
from models.user import order, orderResponse
from database.connection import db 
from bson import ObjectId

router = APIRouter(prefix="/order", tags=["Order"])

@router.post("/create-order", response_model=orderResponse)
async def create_order(order: order):
    order_dict = order.model_dump()
    print(order_dict["order_details"])
    order_dict = await db.orders.find_one({"order_id": order_dict["order_id"]})
    if order_dict:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Order with this ID already exists"
            )
    result = await db.orders.insert_one(order_dict) 
    order_dict["_id"] = str(result.inserted_id)
    return orderResponse(**order_dict)

@router.put('/update-order/{order_id}', response_model=orderResponse)
async def update_order(order_id: str, order: order):
    order_dict = order.model_dump()
    await db.orders.update_one({"_id": ObjectId(order_id)}, {"$set": order_dict}) 
    order_dict["_id"] = order_id
    return orderResponse(**order_dict)

@router.get("/{order_id}", response_model=orderResponse)
async def get_order(order_id: str):
    order = await db.orders.find_one({"_id": ObjectId(order_id)}) 
    if order:
        order["_id"] = str(order["_id"])
        return orderResponse(**order)
    return {"error": "Order not found"}

@router.delete("/delete-order/{order_id}")
async def delete_order(order_id: str):
    result = await db.orders.delete_one({"_id": ObjectId(order_id)})
    if result.deleted_count:
        return {"message": "Order deleted successfully"}
    return {"error": "Order not found"}

