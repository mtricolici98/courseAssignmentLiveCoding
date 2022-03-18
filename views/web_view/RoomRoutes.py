from flask import jsonify, session, Blueprint

from app import app
from services.DataService import DataService
from services.RoomService import RoomService
from views.web_view.view_utils import login_required

rooms_view = Blueprint('room_routes', __name__)


@app.route('/room/list', methods=['GET'])
@login_required
def get_room_list():
    print(session.get('user'), 'requested rooms list')
    data_service = DataService()
    rooms = RoomService(data_service).get_all_rooms()
    return jsonify([room.to_dict() for room in rooms])
