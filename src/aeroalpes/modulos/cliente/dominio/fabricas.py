from dataclasses import dataclass
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.seedwork.dominio.entidades import Entidad
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural
from aeroalpes.modulos.cliente.dominio.reglas import NombreValido, EmailValido, CedulaValida, FechaNacimientoValida, FechaNacimientoFutura


@dataclass
class FabricaClientes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            print( "FabricaClientes: ", obj)
            cliente_natural: ClienteNatural = mapeador.dto_a_entidad(obj)
            self.validar_regla(NombreValido(cliente_natural.nombre))
            self.validar_regla(EmailValido(cliente_natural.email))
            self.validar_regla(CedulaValida(cliente_natural.cedula))
            self.validar_regla(FechaNacimientoValida(cliente_natural.fecha_nacimiento))
            self.validar_regla(FechaNacimientoFutura(cliente_natural.fecha_nacimiento))
            return cliente_natural
