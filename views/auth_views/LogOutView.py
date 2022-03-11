from views.auth_views.LoginView import LoginView
from views.auth_views.RegistrationView import RegistrationView


class LogOutView:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice

    def init_view(self):
        print('Bye')
        self.userService.log_out()
