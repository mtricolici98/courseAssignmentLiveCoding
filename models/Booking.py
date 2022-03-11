from dataclasses import dataclass
from datetime import datetime

from constants.constants import DATE_TIME_FORMAT
from models.Room import Room
from models.User import User


@dataclass
class Booking:
    room: Room
    from_date: datetime
    to_date: datetime
    user: User

    def to_dict(self):
        return dict(
            room=dict(number=self.room.number),
            from_date=self.from_date.strftime(DATE_TIME_FORMAT),
            to_date=self.to_date.strftime(DATE_TIME_FORMAT),
            user=self.user.to_dict()
        )

    @classmethod
    def from_dict(cls, dict_data, room_data, user):
        return Booking(
            room_data,
            datetime.strptime(dict_data['from_date'], DATE_TIME_FORMAT),
            datetime.strptime(dict_data['to_date'], DATE_TIME_FORMAT),
            user
        )
