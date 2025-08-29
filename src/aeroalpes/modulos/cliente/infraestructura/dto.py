from aeroalpes.config.db import db
import uuid
from datetime import datetime

"""DTOs para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio del cliente

"""

class ClienteNatural(db.Model):
    __tablename__ = "clientes_naturales"
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    cedula = db.Column(db.String, nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.now)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # Relación: un cliente puede tener varios métodos de pago
    metodos_pago = db.relationship("MetodoPago", back_populates="cliente", cascade="all, delete-orphan")

class MetodoPago(db.Model):
    __tablename__ = "metodos_pago"
    id = db.Column(db.UUID, primary_key=True, default=uuid.uuid4)
    nombre = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    token_seguridad = db.Column(db.String, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.now)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.now)

    # ForeignKey -> Cada método de pago pertenece a un cliente
    cliente_id = db.Column(db.UUID, db.ForeignKey("clientes_naturales.id"))
    cliente = db.relationship("ClienteNatural", back_populates="metodos_pago")
