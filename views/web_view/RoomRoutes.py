from flask import jsonify, session, Blueprint, request, g

from app import app
from services.DataService import DataService
from services.RoomService import RoomService
from services.RoomTypeAndClassService import RoomTypeAndClassService
from views.web_view.view_utils import login_required

rooms_view = Blueprint('room_routes', __name__)


@app.route('/room/list', methods=['GET'])
@login_required
def get_room_list():
    print(session.get('user'), 'requested rooms list')
    data_service = DataService()
    rooms = RoomService(data_service).get_all_rooms()
    return jsonify([room.to_dict() for room in rooms])


def validate_room_nr(room_number):
    roomService = RoomService(DataService())
    if not room_number:
        print('No room number provided')
    elif roomService.find_room(room_number):
        print('Room already exists')


def validate_room_type(room_type):
    types = RoomTypeAndClassService(DataService()).ROOM_TYPE_CLASS_MAP.keys()
    if not room_type or room_type not in types:
        print('Empty or invalid type')


def validate_room_class(room_class, room_type):
    classes = RoomTypeAndClassService(DataService()).get_room_class_for_type(room_type)
    if not room_class or room_class not in classes:
        print('Wrong class')


@app.route('/room/create', methods=['POST'])
@login_required
def create_room():
    print(session.get('user'), 'requested to create a room')
    data_service = DataService()  # Getting from globals
    try:
        number = request.get_json().get('number')
        type = request.get_json().get('type')
        room_class = request.get_json().get('room_class')
        validate_room_nr(number)
        validate_room_type(type)
        validate_room_class(room_class, type)
    except Exception as ex:
        return jsonify(str(ex)), 400
    room = RoomService(data_service).create_room(number, type, room_class)
    return jsonify([room.to_dict()])
