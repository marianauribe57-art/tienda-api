# 🛒 tienda-api — Guía 2 FastAPI (SENA ADSO)

API REST de una tienda con **CRUD de productos y categorías**, organizada en varios archivos con `APIRouter` y validación con **Pydantic**.

## 📁 Estructura
```
tienda-api/
├── main.py              # crea la app e incluye los routers
├── requirements.txt
└── routers/
    ├── __init__.py      # marca la carpeta como paquete
    ├── productos.py     # modelo + CRUD de productos
    └── categorias.py    # modelo + CRUD de categorías
```

## ▶️ Cómo ejecutarlo
```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Abrir: http://127.0.0.1:8000/docs

Video Demostrativo: https://drive.google.com/file/d/10GQ6e9OKB6kJd49OD09_HO60BMmHY2Qu/view?usp=drive_link

## 🔗 Endpoints
| Operación | Método | Ruta | Éxito | Error |
|---|---|---|---|---|
| Listar | GET | /productos · /categorias | 200 | — |
| Obtener uno | GET | /{recurso}/{id} | 200 | 404 |
| Crear | POST | /productos · /categorias | 201 | 422 |
| Actualizar | PUT | /{recurso}/{id} | 200 | 404 / 422 |
| Eliminar | DELETE | /{recurso}/{id} | 200 | 404 |

## 🧪 Ejemplos de body (JSON)
Producto: `{"nombre": "Audifonos", "precio": 90000, "categoria": "Audio"}`
Categoría: `{"nombre": "Gaming"}`

> Los datos viven en memoria: al reiniciar el servidor vuelven a los iniciales.
