from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Servicio de Traductor Invertido 🔄")


origins = os.getenv("ALLOWED_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/invertir")
def invertir_texto(texto: str):
    """Invierte cualquier texto enviado"""
    if not texto.strip():
        raise HTTPException(status_code=400, detail="¡El texto no puede estar vacío!")
    return {
        "original": texto,
        "invertido": texto[::-1], 
        "longitud": len(texto)
    }

