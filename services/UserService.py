from models.User import User
from services.DataService import DataService
from services.UserGroupService import UserGroupService


class UserService:

    def __init__(self, data_service: DataService):
        self.logged_in_user = None
        self.data_service = data_service

    def log_in(self, username, password):
        users = self.data_service.get_users()
        for user in users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                return True
        return False

    def log_out(self):
        self.logged_in_user = None

    def register(self, username, password, group_name):
        if not self.validate_name(username):
            raise Exception('Invalid user name for registration')
        users = self.data_service.get_users()
        new_user = User(username, password, UserGroupService.get_user_group_by_name(group_name))
        users.append(new_user)
        self.data_service.save_users()

    def validate_name(self, name):
        for user in self.data_service.get_users():
            if user.username == name:
                return False
        return True
