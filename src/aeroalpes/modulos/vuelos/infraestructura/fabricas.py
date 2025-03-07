""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field

from aeroalpes.modulos.vuelos.dominio.repositorios import (
    RepositorioProveedores, RepositorioReservas)
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import (RepositorioProveedoresSQLite,
                           RepositorioReservasSQLite)


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas:
            return RepositorioReservasSQLite()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()