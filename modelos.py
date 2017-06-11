# -*- coding: utf-8 -*-
from openerp import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do task'
    numero = fields.Char('Num Pedido')
    name = fields.Char('Descripcion', required=True)
    is_done = fields.Boolean('Finalizado')
    active = fields.Boolean('Activo', default=True)
    fecha = fields.Datetime('Fecha', default=fields.Date.today)
    urgencia = fields.Char('Nivel de urgencia')

    @api.one
    def do_toggle_done(self):
        # print self.env.context
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True