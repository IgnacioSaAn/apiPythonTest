from sqlalchemy.orm import Session
from . import models

def get_usuarios(db: Session):
    return db.query(models.Usuario).all()
