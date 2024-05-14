from fastapi import APIRouter
from models import ProductModel
from exceptions import BadRequestException, NotFoundException
ProductsRouter =APIRouter(prefix="/products", tags=["Products"])

products:list[ProductModel] = []

@ProductsRouter.get("",response_model= list[ProductModel])
async def get_products()->list[ProductModel]: 
    return products

@ProductsRouter.post("",status_code=201, response_model=ProductModel)
async def create_products(newProduct:ProductModel)->ProductModel:
    products.append(newProduct)
    for product in products:
        if product.id == newProduct.id:
            return newProduct
    raise BadRequestException

@ProductsRouter.get("/{product_id}",response_model=ProductModel)
async def get_product_by_id(product_id:int)->ProductModel:
    for product in products:
        if product.id ==product_id:
            return product
    raise NotFoundException

