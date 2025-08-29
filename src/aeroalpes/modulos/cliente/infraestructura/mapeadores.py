from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural as ClienteNaturalDominio
from aeroalpes.modulos.cliente.dominio.objetos_valor import MetodoPago as MetodoPagoDominio, TipoMetodoPago
from aeroalpes.modulos.cliente.infraestructura.dto import MetodoPago as MetodoPagoDTO, ClienteNatural as ClienteNaturalDTO


class MapeadorClienteNatural(Mapeador):
    def obtener_tipo(self) -> type:
        return ClienteNaturalDTO
    
    def entidad_a_dto(self, entidad: ClienteNaturalDominio) -> ClienteNaturalDTO:
        return ClienteNaturalDTO(id=entidad.id, nombre=entidad.nombre, email=entidad.email, cedula=entidad.cedula, fecha_nacimiento=entidad.fecha_nacimiento)
        
    def dto_a_entidad(self, dto: ClienteNaturalDTO) -> ClienteNaturalDominio:
        return ClienteNaturalDominio(id=dto.id, nombre=dto.nombre, email=dto.email, cedula=dto.cedula, fecha_nacimiento=dto.fecha_nacimiento)

    def _procesar_metodo_pago(self, metodo_pago: MetodoPagoDominio) -> MetodoPagoDTO:
        metodo_pago_dto = MetodoPagoDTO()
        metodo_pago_dto.id = str(metodo_pago.id) if hasattr(metodo_pago, 'id') else ""
        metodo_pago_dto.nombre = metodo_pago.nombre
        metodo_pago_dto.tipo = metodo_pago.tipo.value
        metodo_pago_dto.token_seguridad = metodo_pago.token_seguridad
        return metodo_pago_dto    
        


class MapeadorMetodoPago(Mapeador):
    def obtener_tipo(self) -> type:
        return MetodoPagoDTO
    
    def entidad_a_dto(self, entidad: MetodoPagoDominio) -> MetodoPagoDTO:
        return self._procesar_metodo_pago(entidad)
    
    def dto_a_entidad(self, dto: MetodoPagoDTO) -> MetodoPagoDominio:
        # Convertir string a enum
        tipo_metodo = TipoMetodoPago.TARJETA_CREDITO
        for tipo_enum in TipoMetodoPago:
            if tipo_enum.value == dto.tipo:
                tipo_metodo = tipo_enum
                break
        
        return MetodoPagoDominio(
            nombre=dto.nombre,
            tipo=tipo_metodo,
            token_seguridad=dto.token_seguridad
        )

    def _procesar_metodo_pago(self, metodo_pago: MetodoPagoDominio) -> MetodoPagoDTO:
        metodo_pago_dto = MetodoPagoDTO()
        metodo_pago_dto.id = str(metodo_pago.id) if hasattr(metodo_pago, 'id') else ""
        metodo_pago_dto.nombre = metodo_pago.nombre
        metodo_pago_dto.tipo = metodo_pago.tipo.value
        metodo_pago_dto.token_seguridad = metodo_pago.token_seguridad
        return metodo_pago_dto