# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class tienda(osv.osv):
    _name = 'co.tienda'
    _description = 'CO Tienda'


    _columns = {
        'name': fields.char('Nombre de la Tienda'),
        'address':fields.char('Direccion'),
  
    }

tienda()