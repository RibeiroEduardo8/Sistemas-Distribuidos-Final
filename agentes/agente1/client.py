from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from bardapi import Bard
import uvicorn

# Configuração da API do Bard
os.environ['_BARD_API_KEY'] = "lygVXnlCDn7Ixhmh/AieeS07vq6KDxqugy"

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (pode restringir a um domínio específico)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

class CafeCaracteristicas(BaseModel):
    tipo_cafe: str
    acidez: str
    corpo: str
    doçura: str

@app.post("/enviar-dados")
def processar_recomendacao(cafe: CafeCaracteristicas):
    # Envia os dados para o serviço de recomendação de cor
    resposta = requests.post("http://localhost:8000/recomendar-xicara", json={
        "acidez": cafe.acidez,
        "corpo": cafe.corpo,
        "doçura": cafe.doçura
    })
    
    if resposta.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao obter a recomendação de cor.")
    
    cor_recomendada = resposta.json().get("cor_recomendada", "")
    
    if not cor_recomendada:
        raise HTTPException(status_code=400, detail="Nenhuma cor recomendada encontrada.")
    
    # Gera a mensagem com base na cor recomendada
    input_text = f"Monte para o produtor de café uma frase curta falando que a melhor xícara para ele servir seu café será da cor: {cor_recomendada}"
    mensagem = Bard().get_answer(input_text)['content']
    
    return {"mensagem": mensagem}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
