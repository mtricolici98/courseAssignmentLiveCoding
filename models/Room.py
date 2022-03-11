from dataclasses import dataclass


@dataclass(eq=True)
class Room:
    number: str
    price: str
    type: str
    room_class: str

    @classmethod
    def from_dict(cls, dict_data):
        return cls(dict_data['number'], dict_data['price'], dict_data['type'], dict_data['room_class'])

    def to_dict(self):
        return dict(
            number=self.number,
            price=self.price,
            type=self.type,
            room_class=self.room_class
        )
