from dataclasses import dataclass
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from aeroalpes.modulos.cliente.infraestructura.repositorios import RepositorioClientesSQLite
from aeroalpes.modulos.cliente.infraestructura.excepciones import ExcepcionFabrica



@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        print(f"Creando objeto: {obj}")
        if obj == RepositorioClientes:
            return RepositorioClientesSQLite()
        else:
            raise ExcepcionFabrica()
