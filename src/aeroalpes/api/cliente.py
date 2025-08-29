import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.cliente.aplicacion.servicios import ServicioCliente
from aeroalpes.modulos.cliente.aplicacion.dto import ClienteNaturalDTO
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio
from flask import request, Response
from aeroalpes.modulos.cliente.aplicacion.mapeadores import MapeadorUsuarioDTOJson


bp = api.crear_blueprint('cliente', '/cliente')

@bp.route('/cliente_natural', methods=('POST',))
def crear_cliente_natural():
    try:
        usuario_dict = request.json
        map_usuario = MapeadorUsuarioDTOJson()
        usuario_dto = map_usuario.externo_a_dto(usuario_dict)
        sr = ServicioCliente()
        dto_final = sr.crear_cliente_natural(usuario_dto)
        return map_usuario.dto_a_externo(dto_final)

    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
