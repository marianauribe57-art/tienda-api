"""
routers/auth.py - Autenticacion: login, registro y "quien soy".
"""
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Field

import seguridad

router = APIRouter(prefix="/auth", tags=["Autenticacion"])


class RegistroEntrada(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    nombre: str = Field(min_length=2, max_length=60)
    password: str = Field(min_length=6)


# LOGIN: recibe un formulario usuario/contrasena y devuelve el token
@router.post("/login")
def login(datos: OAuth2PasswordRequestForm = Depends()):
    usuario = seguridad.buscar_usuario(datos.username)
    if usuario is None or not seguridad.verificar_password(datos.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Usuario o contrasena incorrectos")
    token = seguridad.crear_token(usuario["username"])
    return {"access_token": token, "token_type": "bearer"}


# REGISTRO (Ejercicio 3): crea usuarios con rol cliente y contrasena hasheada
@router.post("/registro", status_code=201)
def registro(datos: RegistroEntrada):
    if seguridad.buscar_usuario(datos.username) is not None:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    nuevo = {
        "username": datos.username,
        "nombre": datos.nombre,
        "password": seguridad.hashear_password(datos.password),  # NUNCA en texto plano
        "rol": "cliente",                                       # siempre cliente
    }
    seguridad.usuarios.append(nuevo)
    # No devolvemos la contrasena (ni siquiera el hash)
    return {"mensaje": "Usuario registrado",
            "usuario": {"username": nuevo["username"], "nombre": nuevo["nombre"],
                        "rol": nuevo["rol"]}}


# QUIEN SOY: endpoint protegido de ejemplo
@router.get("/yo")
def quien_soy(usuario: dict = Depends(seguridad.obtener_usuario_actual)):
    return {"username": usuario["username"], "nombre": usuario["nombre"],
            "rol": usuario["rol"]}
