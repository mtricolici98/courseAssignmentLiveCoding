from flask import request, jsonify, Blueprint, g

from app import app
from services.DataService import DataService
from services.UserGroupService import UserGroupService
from services.UserService import UserService

user_views = Blueprint('user_views', __name__)


class ValidationError(Exception):
    pass


def _validate_un(un, user_service):
    if not un or not user_service.validate_name(un):
        raise ValidationError('Invalid user name, please try again.')


def _validate_group(group):
    ugs = UserGroupService()
    if not group or not ugs.validate_user_group_name(group):
        raise ValidationError('Invalid user group, please try again.')


def _validate_pass(passwd):
    if not passwd:
        raise ValidationError('Invalid password, please try again.')


@app.route('/login', methods=['POST'])
def login():
    ds = DataService()
    user_service = UserService(ds)
    r_data = request.get_json()
    if not r_data:
        return 'Bad request', 400
    try:
        user_name = r_data.get('user_name')
        password = r_data.get('password')
        success = user_service.log_in(user_name, password)
        if not success:
            raise ValidationError('Did not login')
    except ValidationError as ex:
        return jsonify(str(ex)), 400
    return {'header-auth': user_service.logged_in_user.username}, 200


@app.route('/register', methods=['POST'])
def register():
    ds = DataService()
    user_service = UserService(ds)
    r_data = request.get_json()
    if not r_data:
        return 'Bad request', 400
    try:
        user_name = r_data.get('user_name')
        password = r_data.get('password')
        group_name = r_data.get('group_name')
        _validate_un(user_name, user_service)
        _validate_group(group_name)
        _validate_pass(password)
    except ValidationError as ex:
        return jsonify(str(ex)), 400
    user_service.register(user_name, password, group_name)
    return jsonify('Success'), 200
