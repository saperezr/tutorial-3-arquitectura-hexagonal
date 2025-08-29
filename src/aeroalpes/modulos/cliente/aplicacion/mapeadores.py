from __future__ import annotations
from datetime import datetime
from aeroalpes.modulos.cliente.aplicacion.dto import MetodoPagoDTO, ClienteNaturalDTO
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.cliente.dominio.entidades import ClienteNatural
from aeroalpes.modulos.cliente.dominio.objetos_valor import MetodoPago
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio


class MapeadorUsuarioDTOJson:
    def externo_a_dto(self, externo: dict) -> ClienteNaturalDTO:
        fecha_nacimiento = None
        fecha_str = externo.get('fecha_nacimiento')
        if fecha_str:
            try:
                fecha_nacimiento = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            except ValueError:
                raise ExcepcionDominio(f"Fecha inválida: {fecha_str}. Debe tener formato YYYY-MM-DD")

        cliente_natural_dto = ClienteNaturalDTO(
            nombre=externo.get('nombre'),
            email=externo.get('email'),
            cedula=externo.get('cedula'),
            fecha_nacimiento=fecha_nacimiento)

        return cliente_natural_dto

    def dto_a_externo(self, dto: ClienteNaturalDTO) -> dict:
        return {
            "id": dto.id,
            "nombre": dto.nombre,
            "email": dto.email,
            "cedula": dto.cedula,
            "fecha_nacimiento": dto.fecha_nacimiento.isoformat() if dto.fecha_nacimiento else None
        }

    def _procesar_metodos_pago(self, metodos_pago_json: list[dict]) -> list[MetodoPagoDTO]:
        metodos_pago_dto: list[MetodoPagoDTO] = []
        for metodo in metodos_pago_json:
            metodos_pago_dto.append(
                MetodoPagoDTO(
                    nombre=metodo.get("nombre"),
                    tipo=metodo.get("tipo"),
                    token_seguridad=metodo.get("token_seguridad")
                )
            )
        return metodos_pago_dto

class MapeadorClienteNatural(RepMap):
    def obtener_tipo(self) -> type:
        return ClienteNatural.__class__
    
    def entidad_a_dto(self, entidad: ClienteNatural) -> ClienteNaturalDTO:
        return ClienteNaturalDTO(
            id=entidad.id,
            nombre=entidad.nombre,
            email=entidad.email,
            cedula=entidad.cedula,
            fecha_nacimiento=entidad.fecha_nacimiento
        )

    def dto_a_entidad(self, dto: ClienteNaturalDTO) -> ClienteNatural:
        return ClienteNatural(
            nombre=dto.nombre,
            email=dto.email,
            cedula=dto.cedula,
            fecha_nacimiento=dto.fecha_nacimiento
        )

    def _procesar_metodos_pago(self, metodos_pago_dto: list[MetodoPagoDTO]) -> list[MetodoPago]:
        metodos_pago: list[MetodoPago] = []
        for metodo in metodos_pago_dto:
            metodos_pago.append(MetodoPago(
                nombre=metodo.nombre,
                tipo=metodo.tipo,
                token_seguridad=metodo.token_seguridad
            ))
        return metodos_pago