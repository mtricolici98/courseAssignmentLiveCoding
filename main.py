from services.DataService import DataService
from services.UserService import UserService
from views.cli_view.MainMenuView import MainMenuView


def main():
    data_service = DataService()
    user_service = UserService(data_service)
    MainMenuView(data_service, user_service).init_view()


if __name__ == '__main__':
    main()
