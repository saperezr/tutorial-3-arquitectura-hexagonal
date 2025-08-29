from aeroalpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from aeroalpes.modulos.cliente.dominio.repositorios import RepositorioMetodosPago
from aeroalpes.modulos.cliente.infraestructura.dto import ClienteNatural, MetodoPago
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural, ClienteEmpresa
from aeroalpes.modulos.cliente.dominio.fabricas import FabricaClientes
from aeroalpes.modulos.cliente.infraestructura.mapeadores import MapeadorClienteNatural
from aeroalpes.modulos.cliente.infraestructura.mapeadores import MapeadorMetodoPago
from aeroalpes.config.db import db

class RepositorioClientesSQLite(RepositorioClientes):

    def __init__(self):
        self._fabrica_cliente_natural: FabricaClientes = FabricaClientes()

    @property
    def fabrica_cliente_natural(self):
        return self._fabrica_cliente_natural


    def obtener_por_id(self, id: str) -> ClienteNatural:
        cliente_natural_dto = db.session.query(ClienteNatural).filter(ClienteNatural.id == id).first()
        return self.fabrica_cliente_natural.crear_objeto(cliente_natural_dto, MapeadorClienteNatural())

    def obtener_todos(self) -> list[ClienteNatural]:
        # TODO
        raise NotImplementedError

    def agregar(self, cliente_natural: ClienteNatural):
        cliente_natural_dto = self.fabrica_cliente_natural.crear_objeto(cliente_natural, MapeadorClienteNatural())
        db.session.add(cliente_natural_dto)
        db.session.commit()

    def actualizar(self, cliente_natural: ClienteNatural):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_natural: ClienteNatural):
        # TODO
        raise NotImplementedError

class RepositorioMetodosPagoSQLite(RepositorioMetodosPago):

    def __init__(self):
        self._fabrica_metodos_pago: FabricaMetodosPago = FabricaMetodosPago()

    @property
    def fabrica_metodos_pago(self):
        return self._fabrica_metodos_pago

    def obtener_por_id(self, id: str) -> MetodoPago:
        metodo_pago_dto = db.session.query(MetodoPago).filter(MetodoPago.id == id).first()
        return self.fabrica_metodos_pago.crear_objeto(metodo_pago_dto, MapeadorMetodoPago())

    def obtener_todos(self) -> list[MetodoPago]:
        # TODO
        raise NotImplementedError
    
    def agregar(self, metodo_pago: MetodoPago):
        metodo_pago_dto = self.fabrica_metodos_pago.crear_objeto(metodo_pago, MapeadorMetodoPago())
        db.session.add(metodo_pago_dto)
        db.session.commit()
