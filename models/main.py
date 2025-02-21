from odoo import http
from odoo.http import request
import requests


class ZohoIntegration(http.Controller):
    @http.route(['/lead_form'], type='http', auth='public', website=True, csrf=False)
    def lead_form(self, **kwargs):
        # course = request.env['op.course'].search([])
        # values = {
        #     'courses': course
        # }
        return request.render('test_web_form_17.lead_web_form_template', )

    @http.route(['/lead_form/submit'], type='http', auth='public', website=True, csrf=False, )
    def lead_form_submit(self, **kwargs):
        print(kwargs, 'oooo')
        source = request.env['leads.sources'].sudo().search([('name', '=', 'Website')], limit=1)

        branch = request.env['op.branch'].sudo().search([('name', '=', 'Nil')])

        request.env['leads.logic'].sudo().create({
            'name': kwargs.get('name'),
            'email_address': kwargs.get('email'),
            'phone_number': kwargs.get('phone'),
            'preferred_course': kwargs.get('course_id'),
            'leads_source': source.id,
            'district': 'nil',
            'mode_of_study': 'nil',
            # 'remarks_lead_user_id': remarks.id,
            'college_name': 'nil',
            'course_type': 'nil',
            'academic_year': '2025-2026',
            'lead_quality': 'new',


        })

        return request.render('test_web_form_17.tmp_lead_enquire_form_success')

