from sqlalchemy import Column, Integer, String, Float
from core.database import Base


class Product(Base):
    __tablename__ = 'produto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(40), nullable=False)
    descricao = Column(String(40), nullable=False)
    preco = Column(Float, nullable=False)


    def __repr__(self):
        return "Produto %s (%s %s)" % (self.id, self.descricao, self.preco)
