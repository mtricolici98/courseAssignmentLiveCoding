from services.RoomService import RoomService


class RoomList:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice
        self.room_service = RoomService(dataService)

    def init_view(self):
        rooms = self.room_service.get_all_rooms()
        if not rooms:
            print('No rooms registered')
        for room in rooms:
            print(room)
