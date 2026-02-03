from pydantic import BaseModel

class NutritionResponse(BaseModel):
    alimento: str
    porcao: str
    calorias_kcal: float
    proteinas_g: float
    carboidratos_g: float
    gorduras_g: float
    fibras_g: float
