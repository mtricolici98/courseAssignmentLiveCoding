from services.RoomService import RoomService
from services.RoomTypeAndClassService import RoomTypeAndClassService


class RoomCreate:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice
        self.roomService = RoomService(self.dataService)
        self.roomMapService = RoomTypeAndClassService(self.dataService)

    def init_view(self):
        print('\nWelcome to room creation screen \n')
        room_number = self.get_room_number()
        room_type = self.get_room_type()
        room_class = self.get_room_class(room_type)
        result = self.roomService.create_room(room_number, room_type, room_class)
        print(f'Room {result} successfully created')
        return

    def get_room_number(self):
        while True:
            room_number = input('Input your user name: ')
            if not room_number:
                print('No room number provided')
            elif self.roomService.find_room(room_number):
                print('Room already exists')
            else:
                return room_number

    def get_room_type(self):
        types = self.roomMapService.ROOM_TYPE_CLASS_MAP.keys()
        while True:
            room_type = input(f'Choose room type {",".join(types)}: ')
            if not room_type or room_type not in types:
                print('Empty or invalid type')
            else:
                return room_type

    def get_room_class(self, room_type):
        classes = self.roomMapService.get_room_class_for_type(room_type)
        while True:
            room_class = input(f'Choose room class: {",".join(classes)}')
            if not room_class or room_class not in classes:
                print('Wrong class')
            else:
                return room_class
