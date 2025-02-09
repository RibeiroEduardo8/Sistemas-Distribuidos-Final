from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import uvicorn

app = FastAPI()

class CafeInput(BaseModel):
    acidez: str
    corpo: str
    doçura: str

caracteristicas = [
    {"tipo_de_café": "Arábica", "acidez": "alta", "corpo": "médio", "doçura": "suave", "melhor_cor_xicara": "branca"},
    {"tipo_de_café": "Robusta", "acidez": "baixa", "corpo": "alto", "doçura": "forte", "melhor_cor_xicara": "preta"},
    {"tipo_de_café": "Café expresso", "acidez": "média", "corpo": "médio", "doçura": "suave", "melhor_cor_xicara": "vermelha"},
    {"tipo_de_café": "Café filtrado", "acidez": "alta", "corpo": "baixo", "doçura": "suave", "melhor_cor_xicara": "azul"},
    {"tipo_de_café": "Café com leite", "acidez": "baixa", "corpo": "médio", "doçura": "alta", "melhor_cor_xicara": "bege"}
]

@app.post("/recomendar-xicara")
def recomendar_xicara(cafe: CafeInput):
    entrada = f"acidez {cafe.acidez}, corpo {cafe.corpo}, doçura {cafe.doçura}"

    resposta = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": f'Com base nas características: {entrada}, e na seguinte base de dados: {caracteristicas}, qual é a cor de xícara mais adequada? Responda apenas com a cor.'}
        ]
    )

    return {"cor_recomendada": resposta["message"]["content"].strip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
