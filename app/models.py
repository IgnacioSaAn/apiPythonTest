from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    rol = Column(String(100))
    compania = Column(String(255))

class ManualMarca(Base):
    __tablename__ = "manuales_marca"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    historia = Column(String(1000))
    tipografia = Column(String(255))
    colores = Column(String(255))

class Trazabilidad(Base):
    __tablename__ = "trazabilidad"

    id = Column(Integer, primary_key=True, index=True)
    numero_manual = Column(Integer, ForeignKey("manuales_marca.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    accion = Column(String(255))

    # relaciones ORM (opcional)
    manual = relationship("ManualMarca")
    usuario = relationship("Usuario")