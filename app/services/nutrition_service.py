from sqlalchemy.orm import Session
from app.models.nutrition import NutritionCache
from app.schemas.nutrition import NutritionResponse
from app.services.gemini_client import consultar_nutricao

def normalizar_chave(quantidade: str, alimento: str) -> str:
    return f"{quantidade.strip().lower()}|{alimento.strip().lower()}"

def get_nutrition(
    quantidade: str,
    alimento: str,
    db: Session
) -> NutritionResponse:

    chave = normalizar_chave(quantidade, alimento)

    cached = (
        db.query(NutritionCache)
        .filter(NutritionCache.chave == chave)
        .first()
    )

    # ✅ CACHE HIT
    if cached:
        return NutritionResponse(
            alimento=cached.alimento,
            porcao=cached.porcao,
            calorias_kcal=cached.calorias_kcal,
            proteinas_g=cached.proteinas_g,
            carboidratos_g=cached.carboidratos_g,
            gorduras_g=cached.gorduras_g,
            fibras_g=cached.fibras_g,
        )

    # ❌ CACHE MISS → chama IA
    prompt = f"{quantidade} de {alimento}"
    data = consultar_nutricao(prompt)

    new_cache = NutritionCache(
        chave=chave,
        alimento=alimento.lower(),
        quantidade=quantidade.lower(),
        porcao=data["porcao"],
        calorias_kcal=data["calorias_kcal"],
        proteinas_g=data["proteinas_g"],
        carboidratos_g=data["carboidratos_g"],
        gorduras_g=data["gorduras_g"],
        fibras_g=data["fibras_g"],
    )

    db.add(new_cache)
    db.commit()

    return NutritionResponse(**data)
