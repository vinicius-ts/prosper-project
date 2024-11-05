from fastapi import APIRouter, HTTPException, Query, Request, Depends
from sqlalchemy.orm import Session
from models.product import Product
from core.database import get_session


router = APIRouter()

@router.get("/")
async def list_products(request: Request, session: Session=Depends(get_session)):
    products = session.query(Product).all()
    return products

@router.post("/")
async def create_product(request: Request, session: Session=Depends(get_session)):
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/{product_id}")
async def update_product(request: Request, product_id: int, session: Session=Depends(get_session)):
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/{product_id}")
async def delete_product(request: Request, product_id: int, session: Session=Depends(get_session)):
    raise HTTPException(status_code=404, detail="Product not found")

