from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    name: str = Field(..., description="The name of the product")
    price: float = Field(..., gt=0, description="The price of the product, must be greater than zero")
    description: Optional[str] = Field(None, description="A brief description of the product")
    stock: int = Field(..., ge=0, description="The available stock of the product, must be non-negative")
    category: Optional[str] = Field(None, description="The category of the product")

class ProductResponse(Product):
    id: str = Field(..., description="The unique identifier of the product", alias="_id")

    