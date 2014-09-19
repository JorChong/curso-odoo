# -*- coding: utf-8 -*-

from openerp.osv import osv, fields

class res_users(osv.osv):
    _inherit = 'res.users'


    _columns = {
        'suscriptor_id': fields.one2many('co.suscriptor', 'user_id'),
      
    }

res_users()