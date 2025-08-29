from dataclasses import dataclass, field
from datetime import date
from aeroalpes.seedwork.aplicacion.dto import DTO

# --- Métodos de pago ---
@dataclass(frozen=True)
class MetodoPagoDTO(DTO):
    nombre: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    token_seguridad: str = field(default_factory=str)


# --- Usuario base ---
@dataclass(frozen=True)
class UsuarioDTO(DTO):
    nombre: str = field(default_factory=str)
    email: str = field(default_factory=str)


# --- Cliente Natural ---
@dataclass(frozen=True)
class ClienteNaturalDTO(UsuarioDTO):
    id: str = field(default_factory=str)
    cedula: str = field(default_factory=str)
    fecha_nacimiento: date = field(default_factory=date)


# --- Cliente Empresa ---
@dataclass(frozen=True)
class ClienteEmpresaDTO(UsuarioDTO):
    rut: str = field(default_factory=str)
    razon_social: str = field(default_factory=str)
    fecha_constitucion: str = field(default_factory=str)
