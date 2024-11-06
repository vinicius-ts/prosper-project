from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from models.product import Product, ProductSchema
from core.database import get_session


router = APIRouter()

@router.get("/")
async def list_products(request: Request, session: Session=Depends(get_session)):
    result = await session.execute(select(Product))
    products = result.scalars().all()
    return products

@router.get("/{product_id}")
async def get_product(product_id: int, session: Session=Depends(get_session)):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    product = result.scalars().first()
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

@router.post("/")
async def create_product(product: ProductSchema, session: Session=Depends(get_session)):
    try:
        new_product = Product(**product.model_dump())
        session.add(new_product)
        await session.commit()
        await session.refresh(new_product)
        return JSONResponse(status_code=201, content=jsonable_encoder(new_product))
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{e}")

@router.put("/{product_id}")
async def update_product(product: ProductSchema, product_id: int, session: Session=Depends(get_session)):
    try:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product_found = result.scalars().first()
        if product_found:
            product_found.nome = product.nome
            product_found.descricao = product.descricao
            product_found.preco = product.preco
            await session.commit()
            await session.refresh(product_found)
            return JSONResponse(status_code=201, content=jsonable_encoder(product_found))
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{e}")

@router.delete("/{product_id}")
async def delete_product(product_id: int, session: Session=Depends(get_session)):
    try:
        result = await session.execute(select(Product).where(Product.id == product_id))
        product_found = result.scalars().first()
        if product_found:
            await session.delete(product_found)
            await session.commit()
            return product_found
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"{e}")
