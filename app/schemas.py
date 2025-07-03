from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    rol: str | None = None
    compania: str | None = None

class Usuario(UsuarioCreate):
    id: int

    class Config:
        orm_mode = True

class ManualMarcaCreate(BaseModel):
    titulo: str
    historia: str | None = None
    tipografia: str | None = None
    colores: str | None = None

class ManualMarca(ManualMarcaCreate):
    id: int

    class Config:
        orm_mode = True

class TrazabilidadCreate(BaseModel):
    numero_manual: int
    usuario_id: int
    accion: str | None = None

class Trazabilidad(TrazabilidadCreate):
    id: int
    class Config:
        orm_mode = True
