from flask import request, jsonify, session


def login_required(fn):
    def wrapped_fn(*args, **kwargs):
        if request.headers.get('header-auth', None) == None:
            return jsonify("not allowed"), 401
        session['user'] = request.headers.get('header-auth')
        return fn(*args, **kwargs)

    return wrapped_fn
