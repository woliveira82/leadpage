from app.apis.campaign import campaign
from app.model import Campaign
from app.inc import Response
from flask_jwt_extended import jwt_required
from webargs.flaskparser import parser
from webargs import fields
from flask import request


@campaign.route(None, methods=['GET'])
# @jwt_required()
def get_campaign_list():
    campaign_list = Campaign.query.all()
    return Response(campaign_list).to_dict()


@campaign.route('/<int:campaign_id>', methods=['GET'])
# @jwt_required()
def get_campaign(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    return Response(campaign).to_dict()


@campaign.route(None, methods=['POST'])
# @jwt_required()
def post_campaign():
    json = parser.parse({
        'name': fields.Str(required=True),
        'description': fields.Str(required=True),
    }, request)
    # get user_id from session
    json['user_id'] = 1
    campaign = Campaign.create(**json)
    return Response(campaign).to_dict()

