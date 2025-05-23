# Microservicios con FastAPI

Proyecto demo con dos microservicios independientes y un frontend unificado.

## 🚀 Servicios

1. **Servicio de Consejos Absurdos** (Puerto 8000)

   - GET `/consejo`: Obtiene un consejo aleatorio.
   - POST `/consejo`: Añade un nuevo consejo.
   - GET `/consejo`: Obtiene lista de consejos.
   - DELETE `/consejo/{indice}`: Eliminar consejo.

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

---

## ⚙️ Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes herramientas:

- **Python 3.x**: lenguaje para los microservicios.
- **Node.js y npm**: para el frontend.
- **pip**: gestor de paquetes de Python.
- **uvicorn**: servidor ASGI que ejecuta aplicaciones FastAPI.

---

## 🛠 Instalación y Uso

### 1. Instalación de Dependencias de los Microservicios

Cada microservicio tiene su propio entorno de ejecución. Navega a cada carpeta antes de instalar:

```bash
# Paso 1: Ir a la carpeta del microservicio
cd servicio/consejos  # o cd servicio/invertir

# Paso 2: Instalar dependencias desde requirements.txt
pip install -r requirements.txt

pip install -r requirements.txt: instala todas las librerías necesarias para que el microservicio funcione correctamente, como FastAPI y uvicorn.

cd servicio/consejos
python3 -m uvicorn main:app --reload --port 8000
```

### 2. Iniciar el backend: 

cd servicio/consejos
python3 -m uvicorn main:app --reload --port 8000

cd servicio/invertir
python3 -m uvicorn main:app --reload --port 8001

### 3. Para el frontend:

```bash
cd front
npm install     # Instala dependencias definidas en package.json
npm run start   # Inicia el proyecto (normalmente en http://localhost:3000)
```

