from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import Base, engine, SessionLocal
from app.services.nutrition_service import get_nutrition
from app.schemas.nutrition import NutritionResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Nutricional")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/nutrition", response_model=NutritionResponse)
def nutrition(
    quantidade: str = Query(..., example="100g"),
    alimento: str = Query(..., example="morango"),
    db: Session = Depends(get_db)
):
    return get_nutrition(quantidade, alimento, db)
