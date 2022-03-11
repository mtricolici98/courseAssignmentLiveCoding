class RoomClasses:
    ORDINARY = 'ORDINARY'
    DELUXE = 'DELUXE'
    VIP = 'VIP'

    @classmethod
    def get_all_classes(cls):
        return [cls.ORDINARY, cls.DELUXE, cls.VIP]
