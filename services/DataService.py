from models.Booking import Booking
from models.Room import Room
from models.User import User
from services.UserGroupService import UserGroupService
from services.file.FileService import JsonFileService


class DataService:

    def __init__(self):
        self._bookings = []
        self._rooms = []
        self._users = []
        self._price_map = dict()
        self._initalaize_all()

    def _initalaize_all(self):
        self.get_users()
        self.get_rooms()
        self.get_bookings()

    def get_bookings(self):
        if self._bookings:
            return self._bookings
        fs = JsonFileService('bookings.json')
        data = fs.load_data()
        if data:
            self._bookings = [Booking.from_dict(el) for el in data]  # TODO: Find user, and find room
        return self._bookings

    def get_users(self):
        if self._users:
            return self._users
        fs = JsonFileService('users.json')
        data = fs.load_data()
        if data:
            self._users = [
                User.from_dict(
                    el['username'], el['password'],
                    UserGroupService.get_user_group_by_name(el['group']['name'])
                ) for el in data]
        return self._users

    def get_rooms(self):
        if self._rooms:
            return self._rooms
        fs = JsonFileService('rooms.json')
        data = fs.load_data()
        if data:
            self._rooms = [Room.from_dict(el) for el in data]
        return self._rooms

    def get_room_price_info(self):
        if self._price_map:
            return self._price_map
        fs = JsonFileService('room_prices.json')
        data = fs.load_data()
        if data:
            self._price_map = data
        return self._price_map

    def save_room_price_info(self, room_prices):
        fs = JsonFileService('room_prices.json')
        fs.save_data(self._price_map)

    def save_rooms(self):
        fs = JsonFileService('rooms.json')
        fs.save_data([room.to_dict() for room in self._rooms])

    def save_bookings(self):
        fs = JsonFileService('bookings.json')
        fs.save_data([booking.to_dict() for booking in self._bookings])

    def save_users(self):
        fs = JsonFileService('users.json')
        fs.save_data([user.to_dict() for user in self._users])
