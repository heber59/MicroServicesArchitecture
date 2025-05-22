# Microservicios con FastAPI

Proyecto demo con dos microservicios independientes y un frontend unificado.

## 🚀 Servicios

1. **Servicio de Consejos Absurdos** (Puerto 8000)

   - GET `/consejo`: Obtiene un consejo aleatorio.
   - POST `/consejo`: Añade un nuevo consejo.

2. **Servicio Invertidor de Texto** (Puerto 8001)
   - GET `/invertir?texto=...`: Invierte cualquier texto.

## 🛠️ Instalación

```bash
# Backend (Python)
cd servicio_consejos && pip install -r requirements.txt
cd ../servicio_invertidor && pip install -r requirements.txt

# Frontend (Node.js)
cd ../frontend && npm install
```
