from flask import request, jsonify, session
from functools import wraps


def login_required(fn):
    @wraps(fn)  # Fixes some bugs
    def wrapped_fn(*args, **kwargs):
        if request.headers.get('header-auth', None) == None:
            return jsonify("not allowed"), 401
        session['user'] = request.headers.get('header-auth')
        return fn(*args, **kwargs)

    return wrapped_fn
