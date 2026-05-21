import getpass
from translations import translations


class ATMLogin:

    def __init__(self, language):

        self.user_id = "1234567890"
        self.pin = "123"
        self.lang = translations[language]

    def login(self):

        print(self.lang["welcome"])

        entered_user_id = input(self.lang["enter_user"])
        entered_pin = getpass.getpass(self.lang["enter_pin"])

        if entered_user_id == self.user_id and entered_pin == self.pin:

            print("\n" + self.lang["success"])

        else:

            print("\n" + self.lang["invalid"])