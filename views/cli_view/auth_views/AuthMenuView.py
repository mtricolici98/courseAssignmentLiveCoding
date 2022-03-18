from views.cli_view.auth_views.LoginView import LoginView
from views.cli_view.auth_views.RegistrationView import RegistrationView


class AuthMenuView:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice

    def get_options(self):
        return {
            1: LoginView,
            2: RegistrationView,
        }

    def init_view(self):
        print('1. Login')
        print('2. Register')
        print('0. Exit')
        choice = -1
        while int(choice) not in [0, 1, 2]:
            choice = input('Please choose: ')
        if choice == '0':
            exit()
        self.get_options()[int(choice)](self.dataService, self.userService).init_view()
