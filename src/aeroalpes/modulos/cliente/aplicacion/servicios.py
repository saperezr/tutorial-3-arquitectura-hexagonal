from aeroalpes.seedwork.aplicacion.servicios import Servicio

from aeroalpes.modulos.cliente.dominio.fabricas import FabricaClientes
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural
from aeroalpes.modulos.cliente.infraestructura.repositorios import RepositorioClientes
from aeroalpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio

from .mapeadores import MapeadorUsuarioDTOJson, MapeadorClienteNatural 
from .dto import ClienteNaturalDTO

class ServicioCliente(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_cliente_natural: FabricaClientes = FabricaClientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_cliente_natural(self):
        return self._fabrica_cliente_natural

    def crear_cliente_natural(self, usuario_dto: ClienteNaturalDTO) -> ClienteNaturalDTO:
        map_usuario = MapeadorClienteNatural()
        usuario: ClienteNatural = self.fabrica_cliente_natural.crear_objeto(usuario_dto, MapeadorClienteNatural())
        print(usuario.nombre)
        print(usuario.email)
        print(usuario.cedula)
        print(usuario.fecha_nacimiento)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes)
        repositorio.agregar(usuario)
        return self.fabrica_cliente_natural.crear_objeto(usuario, MapeadorClienteNatural())
