from dataclasses import dataclass


@dataclass
class UserGroup:
    name: str
    permissions: list

    def has_permission(self, permission_name):
        return permission_name in self.permissions


@dataclass
class User:
    username: str
    password: str
    group: UserGroup

    def to_dict(self):
        return dict(
            username=self.username,
            password=self.password,
            group=dict(name=self.group.name),
        )

    @classmethod
    def from_dict(cls, name, password, group):
        return cls(
            name, password, group
        )
