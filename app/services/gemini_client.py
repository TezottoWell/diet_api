import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

SYSTEM_PROMPT = """
Você é um especialista em nutrição.
Responda SEMPRE em JSON válido, seguindo exatamente este formato:

{
  "alimento": "string",
  "porcao": "string",
  "calorias_kcal": number,
  "proteinas_g": number,
  "carboidratos_g": number,
  "gorduras_g": number,
  "fibras_g": number
}

Regras:
- Não escreva texto fora do JSON
- Use valores médios nutricionais
- Se a porção não for informada, assuma 100g
"""

def consultar_nutricao(alimento: str) -> dict:
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=[alimento],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            temperature=0,
        )
    )

    text = response.text
    return json.loads(text)
