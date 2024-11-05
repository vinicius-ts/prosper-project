from fastapi import FastAPI
from routers.product import router as product_router
from core.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(product_router, prefix="/products", tags=["products"])
