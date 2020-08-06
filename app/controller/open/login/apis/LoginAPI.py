from flask import request
from flask.views import MethodView
from app.inc import Response, Parser, Valid
from flask_jwt_extended import create_access_token


class LoginAPI(MethodView):


    def post(self):
        data = Parser(request).parse({
                'username': Valid(required=True),
                'password': Valid(required=True)
        })
        access_token = create_access_token(identity=data['username'])
        return Response({'access_token': access_token}, message='Server is up!').to_dict()
