from abc import ABC
from aeroalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioClientes(Repositorio, ABC):
    ...

class RepositorioMetodosPago(Repositorio, ABC):
    ...