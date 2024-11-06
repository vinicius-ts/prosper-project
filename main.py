import asyncio
from fastapi import FastAPI
from routers.product import router as product_router
from core.database import Base, engine

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def startup_event():
    await init_models()

app = FastAPI(on_startup=[startup_event])

app.include_router(product_router, prefix="/products", tags=["products"])