from fastapi import FastAPI
from routers import  RootRouter, ProductsRouter
app = FastAPI()
app.include_router(RootRouter)
app.include_router(ProductsRouter)

