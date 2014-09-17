# -*- coding: utf-8 -*-

from openerp.osv import osv, fields
from datetime import datetime

tipos=[
    ('oro', 'Plan Oro'), 
    ('plata', 'Plan Plata'),
    ('bronce', 'Plan Bronce'),
]

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'
    _rec_name = 'code'
    _order = 'date_start desc'


    _columns = {
        'code': fields.char('Codigo'),
        'type':fields.selection(tipos, 'Tipo de Suscripcion'),
        'date_start':fields.date('Fecha Inicia de Suscripcion'),
        'date_end':fields.date('Fecha Final de Suscripcion'),
        'active':fields.boolean('Estatus'),
        'suscriptor_id':fields.many2one('co.suscriptor', 'Afiliado'),
    }

    _defaults={

        'active':True,
        'date_start': datetime.now().strftime('%Y-%m-%d'),
        
     }

    def create(self, cr, uid, values, context=None):
        if context is None:
            context = {}

        values.update({ 'code': self.pool.get('ir.sequence').get(cr, uid, 'seq.suscripcion')})
        return super(suscripcion, self).create(cr, uid, values, context=context)
    
suscripcion()