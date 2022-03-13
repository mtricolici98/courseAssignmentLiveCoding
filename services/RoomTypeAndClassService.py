from models.RoomClasses import RoomClasses
from models.RoomTypes import RoomTypes
from services.DataService import DataService


class RoomTypeAndClassService:
    ROOM_TYPE_CLASS_MAP = {
        RoomTypes.SINGLE: [RoomClasses.ORDINARY, RoomClasses.DELUXE],
        RoomTypes.DOUBLE: [RoomClasses.ORDINARY, RoomClasses.DELUXE],
        RoomTypes.APARTMENT: [RoomClasses.VIP],
    }

    ROOM_TYPE_CLASS_PRICE_MAP = {
        (RoomTypes.SINGLE, RoomClasses.ORDINARY): 50,
        (RoomTypes.DOUBLE, RoomClasses.ORDINARY): 80,
        (RoomTypes.SINGLE, RoomClasses.DELUXE): 75,
        (RoomTypes.DOUBLE, RoomClasses.DELUXE): 100,
        (RoomTypes.APARTMENT, RoomClasses.VIP): 200,
    }

    def __init__(self, dataService: DataService):
        self.dataService = dataService
        self.ROOM_TYPE_CLASS_PRICE_MAP = self.dataService.get_room_price_info() or self.ROOM_TYPE_CLASS_PRICE_MAP
        self.dataService.save_room_price_info(self.ROOM_TYPE_CLASS_PRICE_MAP)

    @classmethod
    def get_room_class_for_type(cls, type_name):
        return cls.ROOM_TYPE_CLASS_MAP[type_name]

    def get_price_for_type_and_class(self, type_name, class_name):
        return self.ROOM_TYPE_CLASS_PRICE_MAP[(type_name, class_name)]
