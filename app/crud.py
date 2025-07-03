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

def get_manuales(db: Session):
    return db.query(models.ManualMarca).all()

def create_manual(db: Session, manual):
    db_manual = models.ManualMarca(
        titulo=manual.titulo,
        historia=manual.historia,
        tipografia=manual.tipografia,
        colores=manual.colores
    )
    db.add(db_manual)
    db.commit()
    db.refresh(db_manual)
    return db_manual

def get_trazabilidades(db: Session):
    return db.query(models.Trazabilidad).all()

def create_trazabilidad(db: Session, traz):
    db_traz = models.Trazabilidad(
        numero_manual=traz.numero_manual,
        usuario_id=traz.usuario_id,
        accion=traz.accion
    )
    db.add(db_traz)
    db.commit()
    db.refresh(db_traz)
    return db_traz
