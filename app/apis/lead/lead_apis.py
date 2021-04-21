from app.apis.lead import lead
from app.inc import Response
from app.model import Lead
from flask import request
from flask_jwt_extended import jwt_required
from webargs import fields
from webargs.flaskparser import parser


@lead.route(None, methods=['GET'])
def get_lead_list():
    lead_list = Lead.query.all()
    return Response(lead_list).to_dict()


@lead.route('/<int:lead_id>', methods=['GET'])
def get_lead(lead_id):
    lead = Lead.query.get(lead_id)
    return Response(lead).to_dict()


@lead.route(None, methods=['POST'])
def post_lead():
    json = parser.parse({
        'email': fields.Email(required=True),
        'first_name': fields.Str(required=False),
    }, request)
    lead = Lead.create(**json)
    return Response(lead).to_dict()
