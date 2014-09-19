# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class multimedia(osv.osv):
    _name = 'co.multimedia'
    _description = 'CO Multimedia'
    _rec_name = 'title'
    _order = 'release_date desc'

    def _compute_stock(self, cr, uid, ids, field_name, arg, context):
        stock_obj = self.pool.get('co.lineas.stock')
        
        if isinstance(ids, (int, long)):
            ids =[ids]
        
        res = {}
        for i in ids:
            lineas_ids = stock_obj.search(cr,uid,[('multimedia_id','=',i), ])
            lineas_brw = stock_obj.browse(cr,uid,lineas_ids)
            res [i] = sum([l.quantity for l in lineas_brw])

        return res

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
        'stock':fields.function(_compute_stock, type='integer'),
    }

multimedia()