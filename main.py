from language import Language
from login import ATMLogin
from menu import ATMMenu


def main():

    print("=" * 40)
    print("ATM MACHINE SYSTEM")
    print("=" * 40)

    # Language Selection
    language = Language()

    selected_language = language.choose_language()

    # Login
    atm = ATMLogin(selected_language)

    login_success = atm.login()

    # Open Menu Only If Login Success
    if login_success:

        menu = ATMMenu()

        menu.show_menu()

    else:

        print("Login Failed")


if __name__ == "__main__":

    main()