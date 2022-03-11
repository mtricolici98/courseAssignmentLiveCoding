from models.Room import Room
from services.RoomTypeAndClassService import RoomTypeAndClassService
from services.DataService import DataService


class RoomService:

    def __init__(self, data_service: DataService):
        self.data_service = data_service
        self._rooms = self.data_service.get_rooms()

    def create_room(self, number, room_type, room_class):
        price = RoomTypeAndClassService(self.data_service).get_price_for_type_and_class(room_type,
                                                                                        class_name=room_class)
        room = Room(number, price, room_type, room_class)
        self._rooms.append(room)
        self.data_service.save_rooms()
        return room

    def get_all_rooms(self):
        return self._rooms

    def find_room(self, number):
        for room in self._rooms:
            if room.number == number:
                return room
