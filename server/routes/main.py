from flask import Blueprint, request, make_response

from server.utils import auth_required, SESSION_TOKEN

bp = Blueprint('main', __name__)

@bp.get('/get/unprotected')
def get_data():
    status_code = 200
    data = {
        "messager": "Me, of course!",
        "message": "Hello, World!",
        "session": SESSION_TOKEN
    }
    return data, status_code

@bp.get('/get/protected')
@auth_required
def get_protected_data():
    status_code = 200
    data = {
        "messager": "Me, of course!",
        "message": "I love cheese... it's gouda!"
    }
    return data, status_code

@bp.post('/post')
def post_data():
    data = request.json
    status_code = 200
    data = {"secret": data['secret']}
    response = make_response(data, status_code)
    return response
