from services.UserGroupService import UserGroupService


class LoginView:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice
        self.userGroupService = UserGroupService()

    def init_view(self):
        print('\nWelcome to login screen \n')
        user_name = self.get_username_input()
        attempts = 3
        while attempts > 0:
            password = self.get_password_input()
            login_successful = self.userService.log_in(user_name, password)
            if not login_successful:
                attempts -= 1
            return
        print('Login successful')
        return

    def get_username_input(self):
        while True:
            user_name = input('Input your user name: ')
            if not user_name or self.userService.validate_name(user_name):
                print('Invalid user name, please try again.')
            else:
                return user_name

    def get_password_input(self):
        while True:
            password = input('Input your new password: ')
            if not password:
                print('Empty password, please try again.')
            else:
                return password
