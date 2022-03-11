class RoomTypes:
    SINGLE = 'SINGLE'
    DOUBLE = 'DOUBLE'
    APARTMENT = 'APARTMENT'

    @classmethod
    def get_all_room_types(cls):
        return [cls.SINGLE, cls.DOUBLE, cls.APARTMENT]
