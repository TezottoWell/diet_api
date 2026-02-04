from fastapi import FastAPI, Depends, Query, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from app.core.database import Base, engine, SessionLocal
from app.services.nutrition_service import get_nutrition
from app.schemas.nutrition import NutritionResponse
from app.core.config import API_TOKEN

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Nutricional")

# Security
api_key_header = APIKeyHeader(name="token", auto_error=False)

async def verify_token(token: str = Security(api_key_header)):
    if API_TOKEN and token == API_TOKEN:
        return token
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Token invalido ou ausente"
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/nutrition", response_model=NutritionResponse, dependencies=[Depends(verify_token)])
def nutrition(
    quantidade: str = Query(..., example="100g"),
    alimento: str = Query(..., example="morango"),
    db: Session = Depends(get_db)
):
    return get_nutrition(quantidade, alimento, db)
