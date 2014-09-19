# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class solicitud(osv.osv):
    _name = 'co.solicitud'
    _description = 'CO Solicitud'
    _rec_name = 'code'
    _order = 'requested_date desc'


    _columns = {
        'code': fields.char('Codigo'),
        'suscriptor_id': fields.many2one('co.suscriptor', 'Afiliado'),
        'multimedia_id': fields.many2one('co.multimedia', 'Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio', 'Tipo de Medio'),
        'tienda_id': fields.many2one('co.tienda', 'Origen'),
        'requested_date': fields.date('Fecha solicitada'),
        'qty_day': fields.integer('Duracion (en dias)'),
        
    }

solicitud()