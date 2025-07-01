from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    rol: str | None = None
    compania: str | None = None