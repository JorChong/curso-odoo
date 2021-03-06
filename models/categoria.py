# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class categoria(osv.osv):
    _name = 'co.categoria'
    _description = 'CO Categoria'
    _rec_name = 'name'
    _order = 'description desc'



    _columns = {
        'name': fields.char('Nombre'),
        'description':fields.text('Descripcion'),
        'parent_id':fields.many2one('co.categoria', 'Padre'),
        'child_ids':fields.one2many(
            'co.categoria', 
            'parent_id', 
            'Sub-Categorias'),

    }

categoria()