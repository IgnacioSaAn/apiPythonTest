from sqlalchemy.orm import Session
from . import models

def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

def crear_usuario(db: Session, usuario):
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        rol=usuario.rol,
        compania=usuario.compania
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario
