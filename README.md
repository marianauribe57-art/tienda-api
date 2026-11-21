# 🛒 tienda-api — Serie APIs con FastAPI (SENA ADSO)

API REST de una tienda que crece guía a guía. Cada guía queda marcada con un **tag** en GitHub.
Equipo: Mariana Uribe Muñoz · Valeria Usuga — Instructor: Mateo Arroyave

| Guía | Tema | Ver el código de esa guía |
|---|---|---|
| 1 | Primera mini-API (proyecto aparte) | [mini-api-catalogo](https://github.com/marianauribe57-art/mini-api-catalogo) |
| 2 | CRUD de productos y categorías con `APIRouter` | [tag guia-2](https://github.com/marianauribe57-art/tienda-api/tree/guia-2) |
| 3 | 🔒 Seguridad: login JWT, bcrypt y roles | [tag guia-3](https://github.com/marianauribe57-art/tienda-api/tree/guia-3) |

## 📁 Estructura
```
tienda-api/
├── main.py              # crea la app e incluye los routers
├── seguridad.py         # (Guía 3) hashing, usuarios, token JWT y dependencias
├── requirements.txt
├── routers/
│   ├── __init__.py      # marca la carpeta como paquete
│   ├── auth.py          # (Guía 3) /auth/login · /auth/registro · /auth/yo
│   ├── productos.py     # modelo + CRUD de productos
│   └── categorias.py    # modelo + CRUD de categorías
├── capturas_guia2/      # evidencias Guía 2 (EV03 y EV04)
└── capturas_guia3/      # evidencias Guía 3 (EV03 y EV04)
```

## ▶️ Cómo ejecutarlo
```bash
python -m venv venv
# Windows:  venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Abrir: http://127.0.0.1:8000/docs → botón **Authorize** para iniciar sesión

## 🔗 Endpoints
| Operación | Método | Ruta | Éxito | Error | Seguridad (Guía 3) |
|---|---|---|---|---|---|
| Listar | GET | /productos · /categorias | 200 | — | 🌐 Público |
| Obtener uno | GET | /{recurso}/{id} | 200 | 404 | 🌐 Público |
| Crear | POST | /productos · /categorias | 201 | 401 / 422 | 🔑 Token |
| Actualizar | PUT | /{recurso}/{id} | 200 | 401 / 404 / 422 | 🔑 Token |
| Eliminar | DELETE | /{recurso}/{id} | 200 | 401 / 403 / 404 | 👑 Solo admin |

### Autenticación (Guía 3)
| Método | Ruta | Descripción |
|---|---|---|
| POST | /auth/login | Usuario y contraseña (formulario) → `access_token` (expira en 30 min) |
| POST | /auth/registro | Crea un usuario con rol cliente y contraseña hasheada |
| GET | /auth/yo | 🔑 Devuelve quién es el dueño del token |

### 👤 Usuarios de prueba
| Usuario | Contraseña | Rol |
|---|---|---|
| admin | admin123 | admin |
| ana | ana123 | cliente |

## 🧪 Ejemplos de body (JSON)
Producto: `{"nombre": "Audifonos", "precio": 90000, "categoria": "Audio"}`
Categoría: `{"nombre": "Gaming"}`

## 🎥 Videos
- Guía 2: https://drive.google.com/file/d/10GQ6e9OKB6kJd49OD09_HO60BMmHY2Qu/view?usp=drive_link
- Guía 3: https://drive.google.com/file/d/1DSTeWSUOiyQJxry_CjXRixdvjJB2X-DX/view?usp=sharing

> Los datos viven en memoria: al reiniciar el servidor vuelven a los iniciales (y se pierden los usuarios registrados).
