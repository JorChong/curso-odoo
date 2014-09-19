# -*- coding: utf-8 -*-

from openerp.report import report_sxw

class listado_multimedia(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(listado_multimedia,self).__init__(cr, uid, name, context=context)
        self.localcontext.update({'get_medios':self._get_medios,})

    def _get_medios(self, multimedia):
        medios_str=''
        for m in multimedia.medio_ids:
            medios_str+='%s, %s' % (m.name, medios_str)
        return medios_str

report_sxw.report_sxw('report.listado.multimedia','co.multimedia','curso_odoo/reports/listado_multimedia.rml',parser=listado_multimedia)