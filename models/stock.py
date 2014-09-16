# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class lineas_stock(osv.osv):
    _name = 'co.lineas.stock'
    _description = 'CO lineas_stock'


    _columns = {
        'multimedia_id': fields.many2one('co.multimedia','Multimedia'),
        'medio_id': fields.many2one('co.tipo.medio','Tipo de Medio'),
        'tienda_id': fields.many2one('co.tienda','Tienda'),
        'quantity': fields.integer('Cantidad'),
    }

lineas_stock()


class tienda(osv.osv):
    _inherit = 'co.tienda'

    _columns = {
        'line_ids': fields.one2many('co.lineas.stocka','tienda_id', 'Stock'),
     
    }

tienda()