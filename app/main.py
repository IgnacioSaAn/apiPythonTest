from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

# crear tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o restringir a tu dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

@app.get("/manuales")
def leer_manuales(db: Session = Depends(get_db)):
    manuales = crud.get_manuales(db)
    return [
        {
            "id": m.id,
            "titulo": m.titulo,
            "historia": m.historia,
            "tipografia": m.tipografia,
            "colores": m.colores
        }
        for m in manuales
    ]

@app.post("/manuales")
def crear_manual(manual: schemas.ManualMarcaCreate, db: Session = Depends(get_db)):
    nuevo_manual = crud.create_manual(db, manual)
    return {
        "id": nuevo_manual.id,
        "titulo": nuevo_manual.titulo,
        "historia": nuevo_manual.historia,
        "tipografia": nuevo_manual.tipografia,
        "colores": nuevo_manual.colores
    }

@app.get("/trazabilidad")
def leer_trazabilidades(db: Session = Depends(get_db)):
    trazas = crud.get_trazabilidades(db)
    return [
        {
            "id": t.id,
            "numero_manual": t.numero_manual,
            "usuario_id": t.usuario_id,
            "accion": t.accion
        }
        for t in trazas
    ]

@app.post("/trazabilidad")
def crear_trazabilidad(traz: schemas.TrazabilidadCreate, db: Session = Depends(get_db)):
    nueva_traza = crud.create_trazabilidad(db, traz)
    return {
        "id": nueva_traza.id,
        "numero_manual": nueva_traza.numero_manual,
        "usuario_id": nueva_traza.usuario_id,
        "accion": nueva_traza.accion
    }
