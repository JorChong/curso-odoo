# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

tipos=[
    ('oro', 'Plan Oro'), 
    ('plata', 'Plan Plata'),
    ('bronce', 'Plan Bronce'),
]

class suscripcion(osv.osv):
    _name = 'co.suscripcion'
    _description = 'CO Suscripcion'


    _columns = {
        'code': fields.char('Codigo'),
        'type':fields.selection(tipos, 'Tipo de Suscripcion'),
        'date_start':fields.date('Fecha Inicia de Suscripcion'),
        'date_end':fields.date('Fecha Final de Suscripcion'),
        'active':fields.boolean('Estatus'),
        'suscriptor_id':fields.many2one('co.suscriptor', 'Afiliado'),
    }

suscripcion()