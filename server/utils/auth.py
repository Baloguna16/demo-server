import functools
from flask import request, make_response

SESSION_TOKEN = "A-RANDOMLY-GENERATED-SESSION-TOKEN"

def auth_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if request.method == 'GET':
            session = request.cookies.get("sessionToken")
        else:
            session = "Maybe another permission for other request types?"

        if session == SESSION_TOKEN:
            # Do some stuff here if you want
            return view(**kwargs)
        else:
            data = {"message": "Sorry, you don't have permission to see my secret. Go to 'get/unprotected' first."}
            response = make_response(data, 403)
            return response
    return wrapped_view
