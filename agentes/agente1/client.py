from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from bardapi import Bard
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Configuração da API do Bard
os.environ['_BARD_API_KEY'] = "SEU_BARD_API_KEY"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CafeCaracteristicas(BaseModel):
    tipo_cafe: str
    acidez: str
    corpo: str
    doçura: str

@app.post("/enviar-dados")
def processar_recomendacao(cafe: CafeCaracteristicas):
    try:
        # Chama o serviço do main.py via Docker (usa "main" no lugar de localhost)
        resposta = requests.post("http://main:8000/recomendar-xicara", json={
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
        input_text = f"Elabore uma resposta curta dizendo que está é a melhor cor de xicara para ser usada: {cor_recomendada}."
        mensagem = Bard().get_answer(input_text)['content']

        return {"mensagem": mensagem}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
