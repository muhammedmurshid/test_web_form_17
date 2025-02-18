from odoo import http
from odoo.http import request
import requests

class CallBackLeadForm(http.Controller):
    @http.route(['/lead_web_form'], type='http', auth='public', website=True, csrf=False)
    def lead_web_form(self, **kwargs):
        return request.render('test_web_form_17.lead_web_enquire_second_form')

    @http.route(['/lead_form/submit'], type='http', auth='public', website=True, csrf=False)
    def lead_form_submit(self, **kwargs):
        source = request.env['leads.sources'].sudo().search([('name', '=', 'Website')], limit=1)
        remarks = request.env['lead.status'].sudo().search([('name', '=', 'Nil')], limit=1)
        branch = request.env['logic.base.branches'].sudo().search([('branch_name', '=', 'Nil')])
        level = request.env['course.levels'].sudo().search([('name', '=', 'Nil')])
        # Prepare data to send to Zoho
        # zoho_url = "https://crm.zoho.in/crm/WebToLeadForm"
        print(kwargs, 'print')
        # zoho_data = {
        #     'name': kwargs.get('first_name'),
        # }
        request.env['leads.logic'].sudo().create({
            'name': kwargs.get('name'),
            'email_address': kwargs.get('email'),
            'phone_number': kwargs.get('phone'),
            'preferred_course': kwargs.get('course'),
            'leads_source': source.id,
            'district': 'nil',
            'mode_of_study': 'nil',
            'remarks_lead_user_id': remarks.id,
            'college_name': 'nil',
            'course_type': 'nil',
            'academic_year': 'nil',
            'lead_quality': 'nil',
            'course_level': level.id

        })

        return request.render('test_web_form_17.tmp_lead_enquire_second_form_success')

    @http.route(['/lead_enquire_form'], type='http', auth='public', website=True, csrf=False)
    def lead_enquire_form(self, **kwargs):
        return request.render('test_web_form_17.lead_web_enquiry_form')