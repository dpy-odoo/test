# -*- coding: utf-8 -*-

from odoo.addons.website_event.controllers.main import WebsiteEventController
from odoo.http import request

class EventController(WebsiteEventController):

    def _create_attendees_from_registration_post(self, event, registration_data):
        res = super(EventController, self)._create_attendees_from_registration_post(
            event, registration_data)
        # For contact list
        contact_email = request.env['res.partner'].search(
            [('email', '=', res.email)])
        contact_phone = request.env['res.partner'].search(
            [('phone', '=', res.phone)])
        if not contact_email:
            request.env['res.partner'].create({
                'name': res.name,
                'phone': res.phone,
                'email': res.email,
            })
        if not contact_phone:
            request.env['res.partner'].create({
                'name': res.name,
                'phone': res.phone,
                'email': res.email,
            })
        # For Lead list
        # You have mentioned that move the record in contact list if email or phone match that's I've unlink the current record and created this record in contacts.
        lead_email = request.env['crm.lead'].search([('email_from', '=', res.email)])
        lead_phone = request.env['crm.lead'].search([('phone', '=', res.phone)])
        if lead_email:
            for rec in lead_email:
                rec.env['res.partner'].create({
                    'name': res.name,
                    'phone': res.phone,
                    'email': res.email,
                })
                rec.unlink()
        if lead_phone:
            for rec in lead_email:
                rec.env['res.partner'].create({
                    'name': res.name,
                    'phone': res.phone,
                    'email': res.email,
                })
                rec.unlink()
        return res
