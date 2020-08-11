from flask import Blueprint

from .LeadAPI import LeadAPI

leads = Blueprint('leads', __name__)

leads_api = LeadAPI.as_view('leads_api')
leads.add_url_rule(None, view_func=leads_api, methods=['GET', 'POST', 'DELETE'])
