from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import uvicorn

app = FastAPI()

# Modelo para receber as características e tipo de café
class CafeInput(BaseModel):
    tipo_de_cafe: str  # Novo parâmetro: tipo de café
    acidez: str
    corpo: str
    doçura: str

# Base de dados com as características de cada tipo de café
caracteristicas = [
    {"tipo_de_café": "Arábica", "acidez": "alta", "corpo": "médio", "doçura": "suave", "melhor_cor_xicara": "branca"},
    {"tipo_de_café": "Robusta", "acidez": "baixa", "corpo": "alto", "doçura": "forte", "melhor_cor_xicara": "preta"},
    {"tipo_de_café": "Café expresso", "acidez": "média", "corpo": "mediano", "doçura": "suave", "melhor_cor_xicara": "vermelha"},
    {"tipo_de_café": "Café filtrado", "acidez": "alta", "corpo": "baixo", "doçura": "suave", "melhor_cor_xicara": "azul"},
    {"tipo_de_café": "Café com leite", "acidez": "baixa", "corpo": "médio", "doçura": "alta", "melhor_cor_xicara": "bege"},
    {"tipo_de_café": "Arábica", "acidez": "baixa", "corpo": "médio", "doçura": "suave", "melhor_cor_xicara": "amarela"}
]

@app.post("/recomendar-xicara")
def recomendar_xicara(cafe: CafeInput):
    # Agora, a variável 'entrada' inclui o tipo de café
    entrada = f"tipo de café {cafe.tipo_de_cafe}, acidez {cafe.acidez}, corpo {cafe.corpo}, doçura {cafe.doçura}"

    # Agora, a recomendação irá ocorrer com base no tipo de café
    resposta = ollama.chat(
        model="phi3:mini",
        messages=[
            {"role": "user", "content": f'Com base nas características: {entrada}, e na seguinte base de dados: {caracteristicas}, qual é a cor de xícara mais adequada para o tipo de café {cafe.tipo_de_cafe}? Responda apenas com a cor.'}
        ]
    )

    return {"cor_recomendada": resposta["message"]["content"].strip()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
