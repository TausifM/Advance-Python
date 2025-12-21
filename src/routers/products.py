from fastapi import APIRouter, UploadFile, File, Form, Depends
from models.product import Product, ProductResponse
from database.connection import db 
from bson import ObjectId
from typing import List
from utils.cloudinary import upload_multiple_images_to_cloudinary

router = APIRouter(prefix="/products", tags=["Products"])

# CRUD Operations for Products 
# What is CRUD? Create, Read, Update, Delete methods for managing products in the database
# POST /products/create-product - Create a new product
# GET /products/{product_id} - Get product details by ID
# PUT /products/update-product/{product_id} - Update product details by ID
# DELETE /products/delete-product/{product_id} - Delete product by ID
# PATCH /products/partial-update-product/{product_id} - Partially update product details by ID
def product_form(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(...),
    stock: int= Form(...),
    category: str = Form(...)
) -> Product:
    return Product(
        name=name,
        price=price,
        description=description,
        stock=stock,
        category=category
    )
@router.post("/create-product", response_model=ProductResponse)
async def create_product(product: Product = Depends(product_form), images: List[UploadFile] = File(...)):
    product_dict = product.model_dump()
    # image_dict = product_dict["images"]
    image_urls = upload_multiple_images_to_cloudinary(images=images)
    product_dict["images"] = image_urls
    result = await db.products.insert_one(product_dict) # inser_one is the method to insert a document into a MongoDB collection
    product_dict["_id"] = str(result.inserted_id)
    return ProductResponse(**product_dict)


@router.put('/update-product/{product_id}', response_model=ProductResponse)
async def update_product(product_id: str, product: Product):
    product_dict = product.model_dump()
    await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product_dict}) # update_one is the method to update a document in a MongoDB collection
    product_dict["_id"] = product_id
    return ProductResponse(**product_dict)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await db.products.get_one({"_id": ObjectId(product_id)}) 
    if product:
        product["_id"] = str(product["_id"])
        return ProductResponse(**product)
    return {"error": "Product not found"}

@router.delete("/delete-product/{product_id}")
async def delete_product(product_id: str):
    result = await db.products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count:
        return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}

