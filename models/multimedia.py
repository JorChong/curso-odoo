# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'
    _rec_name = 'title'
    _order = 'release_date desc'


    _columns = {
        'title': fields.char('Titulo', required = True),
        'release_date':fields.date('Fecha Publicacion'),
        'code':fields.char('Codigo'),
        'categoria_id':fields.many2one('co.categoria', 'Categoria'),
        'medio_ids':fields.many2many(
            'co.tipo.medio', 
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id'),
    }

multimedia()