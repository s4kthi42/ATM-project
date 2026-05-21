from language import Language
from login import ATMLogin


def main():

    print("*" * 40)
    print("        ATM MACHINE SYSTEM        ")
    print("*" * 40)

    # Language Selection
    language = Language()

    selected_language = language.choose_language()

    # Login System
    atm = ATMLogin(selected_language)

    atm.login()


# Program Starting Point
if __name__ == "__main__":
    main()