from models.User import UserGroup


class UserGroupService:
    USER_GROUPS = []

    GROUP_TO_PERMISSIONS_MAP = {
        'admin': ["create_booking",
                  "cancel_booking",
                  "list_rooms_with_prices",
                  "list_bookings",
                  "create_room",
                  "change_prices", ],
        'guest': ["create_booking",
                  "cancel_booking",
                  "list_rooms_with_prices"
                  ],
        'front_desk': ["create_booking",
                       "cancel_booking",
                       "list_rooms_with_prices",
                       "list_bookings"],
    }

    @classmethod
    def get_user_group_by_name(cls, name):
        for ug in cls.USER_GROUPS:
            if ug.name == name:
                return ug
        else:
            new_user_group = UserGroup(name, cls.GROUP_TO_PERMISSIONS_MAP[name])
            cls.USER_GROUPS.append(new_user_group)
            return new_user_group

    @classmethod
    def get_all_user_groups(cls):
        return cls.GROUP_TO_PERMISSIONS_MAP.keys()

    @classmethod
    def validate_user_group_name(cls, name):
        return name in cls.GROUP_TO_PERMISSIONS_MAP.keys()
