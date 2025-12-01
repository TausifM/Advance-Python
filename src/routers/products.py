from fastapi import APIRouter, HTTPExeption
from models.product import Product, ProductResponse
from database.connection import db 
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/create-product", response_model=ProductResponse)
async def create_product(product: Product):
    new_product = product.model_dump()
    result = await db.products.insert_one(new_product)
    new_product["_id"] = str(result.inserted_id)
    return new_product
