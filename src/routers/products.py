from fastapi import APIRouter
from models.product import Product, ProductResponse
from database.connection import db 
from bson import ObjectId

router = APIRouter(prefix="/products", tags=["Products"])

# CRUD Operations for Products 
# What is CRUD? Create, Read, Update, Delete methods for managing products in the database
# POST /products/create-product - Create a new product
# GET /products/{product_id} - Get product details by ID
# PUT /products/update-product/{product_id} - Update product details by ID
# DELETE /products/delete-product/{product_id} - Delete product by ID
# PATCH /products/partial-update-product/{product_id} - Partially update product details by ID

@router.post("/create-product", response_model=ProductResponse)
async def create_product(product: Product):
    product_dict = product.model_dump()
    result = await db.products.insert_one(product_dict) # inser_one is the method to insert a document into a MongoDB collection
    product_dict["_id"] = str(result.inserted_id)
    return ProductResponse(**product_dict)


@router.put('/update-product/{product_id}', response_model=ProductResponse)
async def update_product(product_id: str, product: Product):
    product_dict = product.model_dump()
    await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product_dict}) # update_one is the method to update a document in a MongoDB collection
    product_dict["_id"] = product_id
    return ProductResponse(**product_dict)