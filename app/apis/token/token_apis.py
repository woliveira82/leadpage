from app.inc import Response
from flask_jwt_extended import jwt_required
from app.apis.token import token


@token.route('/', methods=['GET'])
@jwt_required()
def post_token_test():
    return Response(None, message='This token is valid!').to_dict()
