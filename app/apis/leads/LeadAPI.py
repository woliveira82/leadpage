from flask import request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required

from app.inc import Parser, Response, ResponseException, Valid
from app.model import Lead


class LeadAPI(MethodView):


    @jwt_required
    def get(self, leads_id=None):
        query = {'is_active': True}
        if leads_id:
            query.update({'id': leads_id})
            leads_list = Lead.read(query=query)
            if len(leads_list) == 0:
                return Response({}).to_dict()

            return Response(leads_list[0]).to_dict()

        leads_list = Lead.read(query=query)
        return Response(leads_list).to_dict()
        

    def post(self):
        data = Parser(request).parse({
            'email': Valid(required=True),
            'first_name': Valid(required=True),
            'is_active': Valid(default=True),
            'extra_conf': Valid(),
        })
        lead = Lead(**data).create()
        return Response(lead, 201).to_dict()


    def delete(self):
        data = Parser(request).parse({
            'email': Valid(required=True),
        })
        data.update({'is_active': True})
        leads_list = Lead.read(query=data)
        if len(leads_list) == 0:
            return Response('No active email found', 200).to_dict()
        
        leads = leads_list[0]
        leads.is_active = False
        leads.update()
        return Response(None, 200, 'Successfuly deleted').to_dict()
