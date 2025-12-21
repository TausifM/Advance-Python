import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os
load_dotenv()

# Configuration       
cloudinary.config( 
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), # Your cloud name
    api_key = os.getenv("CLOUDINARY_API_KEY"), # Click 'View API Keys' above to copy your API key
    api_secret = os.getenv("CLOUDINARY_SECRET_KEY"), # Click 'View API Keys' above to copy your API secret
    secure=True
)
print(os.getenv("CLOUDINARY_SECRET_KEY"), os.getenv("CLOUDINARY_API_KEY"), os.getenv("CLOUDINARY_CLOUD_NAME") )
# Upload multiple images to Cloudinary
# async def upload_multiple_images_to_cloudinary(images):
#     uploaded_image_urls = []
#     for file in images:
#         result = cloudinary.uploader.upload(
#             file.file,
#             folder='products_images'
#             )
#         url, options = cloudinary_url(result['public_id'], format=result['format'])
#         uploaded_image_urls.append(url)
#     return uploaded_image_urls

def upload_multiple_images_to_cloudinary(images):
    uploaded_image_urls = []

    for file in images:
        result = cloudinary.uploader.upload(
            file.file,
            folder="products_images"
        )
        uploaded_image_urls.append(result["secure_url"])

    return uploaded_image_urls