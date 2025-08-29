"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import Optional
import uuid

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: int
    ciudad: Ciudad


class TipoTarjeta(Enum):
    VISA = "Visa"
    MASTERCARD = "Mastercard"
    AMERICAN_EXPRESS = "American Express"

@dataclass(frozen=True)
class Tarjeta(ObjetoValor):
    numero: int
    tipo: TipoTarjeta
    cvv: int
    fecha_expiracion: datetime

class TipoCuenta(Enum):
    CORRIENTE = "Corriente"
    AHORRO = "Ahorro"

@dataclass(frozen=True)
class Cuenta(ObjetoValor):
    numero: int
    tipo: TipoCuenta
    cvv: int
    fecha_expiracion: datetime


class TipoMetodoPago(Enum):
    TARJETA_CREDITO = "Tarjeta de Crédito"
    TARJETA_DEBITO = "Tarjeta de Débito"
    TRANSFERENCIA_BANCARIA = "Transferencia Bancaria"
    PSE = "PSE"
    EFECTIVO = "Efectivo"
    CRYPTO = "Criptomonedas"
    WALLET_DIGITAL = "Wallet Digital"


@dataclass(frozen=True)
class MetodoPago(ObjetoValor):
    nombre: str
    tipo: TipoMetodoPago
    token_seguridad: str
    