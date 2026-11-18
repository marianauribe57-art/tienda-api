from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

import seguridad  # Guia 3: logica de login, token y roles

router = APIRouter(prefix="/categorias", tags=["Categorias"])


# Modelo de entrada (sin id: lo asigna el servidor)
class CategoriaEntrada(BaseModel):
    nombre: str


# "Base de datos" en memoria
categorias = [
    {"id": 1, "nombre": "Perifericos"},
    {"id": 2, "nombre": "Pantallas"},
    {"id": 3, "nombre": "Audio"},
]


# LISTAR (publico)  GET /categorias
@router.get("")
def listar_categorias():
    return categorias


# OBTENER UNA (publico)             GET /categorias/{categoria_id}
@router.get("/{categoria_id}")
def obtener_categoria(categoria_id: int):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            return categoria
    raise HTTPException(status_code=404, detail="Categoria no encontrada")


# CREAR (requiere token)                   POST /categorias  (201)
@router.post("", status_code=201)
def crear_categoria(datos: CategoriaEntrada,
                    usuario: dict = Depends(seguridad.obtener_usuario_actual)):
    nuevo_id = max((c["id"] for c in categorias), default=0) + 1
    nueva = {"id": nuevo_id, "nombre": datos.nombre}
    categorias.append(nueva)
    return {"mensaje": "Categoria creada", "categoria": nueva,
            "creado_por": usuario["username"]}


# ACTUALIZAR (requiere token)    PUT /categorias/{categoria_id}
@router.put("/{categoria_id}")
def actualizar_categoria(categoria_id: int, datos: CategoriaEntrada,
                         usuario: dict = Depends(seguridad.obtener_usuario_actual)):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            categoria["nombre"] = datos.nombre
            return {"mensaje": "Categoria actualizada", "categoria": categoria,
                    "actualizado_por": usuario["username"]}
    raise HTTPException(status_code=404, detail="Categoria no encontrada")


# ELIMINAR (requiere rol admin)                DELETE /categorias/{categoria_id}
@router.delete("/{categoria_id}")
def eliminar_categoria(categoria_id: int,
                       admin: dict = Depends(seguridad.requerir_admin)):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            categorias.remove(categoria)
            return {"mensaje": "Categoria eliminada", "categoria": categoria,
                    "eliminado_por": admin["username"]}
    raise HTTPException(status_code=404, detail="Categoria no encontrada")
