from aeroalpes.seedwork.dominio.reglas import ReglaNegocio
from datetime import datetime, date
from .objetos_valor import Nombre, Email, Cedula, MetodoPago, TipoMetodoPago
from .entidades import ClienteNatural, ClienteEmpresa
import re



class NombreValido(ReglaNegocio):
    nombre: Nombre

    def __init__(self, nombre, mensaje='El nombre no es válido'):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        return len(self.nombre) > 0

class EmailValido(ReglaNegocio):
    email: Email

    def __init__(self, email, mensaje='El email no es válido'):
        super().__init__(mensaje)
        self.email = email

    def es_valido(self) -> bool:
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email) is not None

class CedulaValida(ReglaNegocio):
    cedula: Cedula

    def __init__(self, cedula, mensaje='La cédula no es válida'):
        super().__init__(mensaje)
        self.cedula = cedula

    def es_valido(self) -> bool:
        return  self.cedula is not None

class MetodoPagoValido(ReglaNegocio):
    metodo_pago: MetodoPago
    def __init__(self, metodo_pago, mensaje='El método de pago no es válido'):
        super().__init__(mensaje)
        self.metodo_pago = metodo_pago
    
    def es_valido(self) -> bool:
        return self.metodo_pago.tipo == TipoMetodoPago.TARJETA_CREDITO or self.metodo_pago.tipo == TipoMetodoPago.TARJETA_DEBITO or self.metodo_pago.tipo == TipoMetodoPago.TRANSFERENCIA_BANCARIA or self.metodo_pago.tipo == TipoMetodoPago.PSE or self.metodo_pago.tipo == TipoMetodoPago.EFECTIVO or self.metodo_pago.tipo == TipoMetodoPago.CRYPTO or self.metodo_pago.tipo == TipoMetodoPago.WALLET_DIGITAL

class FechaNacimientoValida(ReglaNegocio):
    fecha_nacimiento: date

    def __init__(self, fecha_nacimiento, mensaje='La fecha de nacimiento no es válida'):
        super().__init__(mensaje)
        self.fecha_nacimiento = fecha_nacimiento

    def es_valido(self) -> bool:
        return self.fecha_nacimiento is not None

class FechaNacimientoFutura(ReglaNegocio):
    fecha_nacimiento: date

    def __init__(self, fecha_nacimiento, mensaje='La fecha de nacimiento no puede ser futura'):
        super().__init__(mensaje)
        self.fecha_nacimiento = fecha_nacimiento

    def es_valido(self) -> bool:
        return self.fecha_nacimiento < datetime.now().date()