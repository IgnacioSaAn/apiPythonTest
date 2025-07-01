from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

# crear tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/usuarios")
def leer_usuarios(db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db)
    return [
        {
            "id": u.id,
            "nombre": u.nombre,
            "email": u.email,
            "rol": u.rol,
            "compania": u.compania
        }
        for u in usuarios
    ]

@app.post("/usuarios")
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = crud.crear_usuario(db, usuario)
    return {
        "id": nuevo_usuario.id,
        "nombre": nuevo_usuario.nombre,
        "email": nuevo_usuario.email,
        "rol": nuevo_usuario.rol,
        "compania": nuevo_usuario.compania
    }
