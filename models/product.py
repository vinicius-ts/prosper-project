from sqlalchemy import Column, Integer, String, Float
from core.database import Base
from pydantic import BaseModel


class Product(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False)
    descricao = Column(String(40), nullable=False)
    preco = Column(Float, nullable=False)


    def __repr__(self):
        return "Produto %s (%s %s)" % (self.id, self.descricao, self.preco)
    
class ProductSchema(BaseModel):
    nome: str
    descricao: str
    preco: float

    class Config:
        from_attributes = True
