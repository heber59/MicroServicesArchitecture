from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random
import os
from dotenv import load_dotenv
from typing import List


load_dotenv()

app = FastAPI(
    title="API de Consejos Universitarios",
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
    "¿Falto a la introduccion? La sugerencia es asistir, pues es una especie de ritual donde los jóvenes se inician en la vida universitaria y se constituye en el proceso de adaptación, conocimiento y ubicación de este contexto.\nAllí se arman grupos de trabajo y se establecen relaciones de amistad, lo cual favorece una buena vida universitaria.",
    "¿faltar a clases?  se puede; en últimas, esto es algo que esperan los jóvenes con ansias. Sin embargo, esta ausencia genera consecuencias negativas como atrasarse en los temas vistos y perder la secuencia de los mismos, lo cual no permite integrar el conocimiento o incluso quedar excluido, pues en algunas universidades el reglamento exige la asistencia permanente a las sesiones e incluso puede considerar la incidencia de las fallas en las notas.",
    "¿Qué servicios me presta la universidad? unidades de apoyo financiero, bienestar universitario y programas de intercambio, de doble titulación, de acompañamiento y de tutorías, entre otros.",
    "¿Qué tan autónomo voy a ser? actualmente la mayoría de universidades adelantan programas de acompañamiento en los que vinculan a la familia, y por esta vía ellos se enteran de la realidad académica de sus hijos. Así que el estudiante es autónomo y esto implica que sea responsable",
    "Si me gustan los deportes o la música, ¿puedo cultivar estas aficiones? Claro que sí, bienestar universitario tiene diferentes departamentos de bienestar universitario cuentan con una amplia oferta en diferentes disciplinas deportivas, culturales y artísticas.",
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
    """Añade un nuevo consejo universitario"""
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

