from core.database import Base, engine

Base.metadata.create_all(engine)
