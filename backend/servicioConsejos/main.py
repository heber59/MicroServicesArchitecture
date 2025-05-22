from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import os
from dotenv import load_dotenv
from typing import List


load_dotenv()

app = FastAPI(
    title="API de Consejos Absurdos",
    description="Microservicio para generar y almacenar consejos hilarantes 🤪"
)


origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


consejos_db: List[str] = [
    "Si tienes frío, métete en el microondas (no lo hagas).",
    "Habla con las plantas, pero ignora sus respuestas."
]

class Consejo(BaseModel):
    texto: str

@app.get("/consejo", tags=["Consejos"])
def obtener_consejo_aleatorio():
    """Devuelve un consejo absurdo al azar"""
    return {"consejo": random.choice(consejos_db)}

@app.get("/consejos", tags=["Consejos"])
def listar_consejos():
    """Lista todos los consejos con sus índices"""
    return {"consejos": {i: consejo for i, consejo in enumerate(consejos_db)}}

@app.post("/consejo", tags=["Consejos"])
def agregar_consejo(consejo: Consejo):
    """Añade un nuevo consejo absurdo"""
    if not consejo.texto.strip():
        raise HTTPException(status_code=400, detail="¡El texto no puede estar vacío!")
    consejos_db.append(consejo.texto)
    return {"mensaje": "✅ Consejo añadido", "indice": len(consejos_db) - 1}

@app.delete("/consejo/{indice}", tags=["Consejos"])
def eliminar_consejo(indice: int):
    """Elimina un consejo por su índice"""
    try:
        consejo_eliminado = consejos_db.pop(indice)
        return {"mensaje": "🗑️ Consejo eliminado", "consejo": consejo_eliminado}
    except IndexError:
        raise HTTPException(status_code=404, detail="❌ Índice no válido")

