from pydantic import BaseModel, Field
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class Order(BaseModel):
    user_id: str
    items: List[OrderItem]
    total_price: float

class OrderResponse(Order):
    id: str = Field(..., description="The unique identifier of the order", alias="_id")
    user_id: str
    items: List[OrderItem]
    total_price: float


