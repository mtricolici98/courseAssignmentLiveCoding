from views.auth_views.LogOutView import LogOutView
from views.user_menus.rooms.RoomCreate import RoomCreate
from views.user_menus.rooms.RoomList import RoomList


class MainUserMenu:

    def __init__(self, dataService, userSerice):
        self.dataService = dataService
        self.userService = userSerice

    def get_options(self):
        return {
            1: {'view': RoomList, 'permission': 'list_rooms_with_prices', 'name': 'List rooms'},
            2: {'view': RoomCreate, 'permission': 'create_room', 'name': 'Create rooms'},
            0: {'view': LogOutView, 'permission': 'create_room', 'name': 'Log out'},
        }

    def init_view(self):
        choice = self.get_choice()
        self.show_sub_view(choice)

    def get_choice(self):
        shown_choices = []
        for key, item in self.get_options().items():
            if self.userService.logged_in_user.group.has_permission(item['permission']):
                print(f"{key}: {item['name']}")
                shown_choices.append(key)
        choice = -1
        while int(choice) not in shown_choices:
            choice = input('Please choose: ')
        return choice

    def show_sub_view(self, choice=-1):
        self.get_options()[int(choice)]['view'](self.dataService, self.userService).init_view()
