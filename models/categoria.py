# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class categoria(osv.osv):
    _name = 'co.categoria'
    _description = 'CO Categoria'


    _columns = {
        'name': fields.char('Nombre'),
        'description':fields.text('Descripcion'),
        'parent_id':fields.may2one('co.categoria', 'Padre'),
        'child_ids':fields.one2many(
            'co.categoria', 
            'parent_id', 
            'Sub-Categorias'),

    }

categoria()