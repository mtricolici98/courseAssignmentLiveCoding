from services.UserGroupService import UserGroupService


class RegistrationView:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice
        self.userGroupService = UserGroupService()

    def init_view(self):
        print('\nWelcome to registration view \n')
        user_name = self.get_username_input()
        password = self.get_password_input()
        group_name = self.get_group_input()
        self.userService.register(user_name, password, group_name)
        print('Registration successful')
        return

    def get_username_input(self):
        while True:
            user_name = input('Input your new user name: ')
            if not user_name or not self.userService.validate_name(user_name):
                print('Invalid user name, please try again.')
            else:
                return user_name

    def get_password_input(self):
        while True:
            password = input('Input your new password: ')
            if not password:
                print('Invalid password, please try again.')
            else:
                return password

    def get_group_input(self):
        while True:
            group_name = input(
                f'Input your user group from {", ".join(self.userGroupService.get_all_user_groups())}: '
            )
            if not group_name or not self.userGroupService.validate_user_group_name(group_name):
                print('Invalid user group, please try again.')
            else:
                return group_name
