from sqlalchemy import Column, String, Float
from app.core.database import Base

class NutritionCache(Base):
    __tablename__ = "nutrition_cache"

    chave = Column(String, primary_key=True, index=True)

    alimento = Column(String)
    quantidade = Column(String)

    porcao = Column(String)
    calorias_kcal = Column(Float)
    proteinas_g = Column(Float)
    carboidratos_g = Column(Float)
    gorduras_g = Column(Float)
    fibras_g = Column(Float)
