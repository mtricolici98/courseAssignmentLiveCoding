from views.auth_views.AuthMenuView import AuthMenuView
from views.user_menus.MainUserMenu import MainUserMenu


class MainMenuView:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice

    def init_view(self):
        while True:
            result = self.print_menu()
            if not result:
                break

    def print_menu(self):
        if self.userService.logged_in_user is None:
            AuthMenuView(self.dataService, self.userService).init_view()
            return True
        else:
            MainUserMenu(self.dataService, self.userService).init_view()
            return True
