from flask.views import MethodView
from app.inc import Response
from flask_jwt_extended import jwt_required


class TokenAPI(MethodView):


    @jwt_required
    def get(self):
        return Response(None, message='This token is valid!').to_dict()
