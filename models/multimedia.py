# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'


    _columns = {
        'title': fields.char('Titulo'),
        'release_ date':fields.date('Fecha Publicacion'),
        'code':fields.char('Codigo'),
        'categorita_id':fields.many2one('co.categoria', 'Categoria'),
        'medio_ids':fields.many2one(
            'co.tipo_medio', 
            'co_multimedia_medio_rel',
            'multimedia_id',
            'medio_id'),
    }

multimedia()