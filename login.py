import getpass


class ATMLogin:

    def __init__(self):

        self.user_id = "1234567890"
        self.pin = "123"

    def login(self):

        print("=" * 40)
        print("ATM LOGIN SYSTEM")
        print("=" * 40)

        entered_user_id = input("Enter User ID: ")
        entered_pin = getpass.getpass("Enter PIN: ")

        if entered_user_id == self.user_id and entered_pin == self.pin:

            print("\nLogin Successful")
            print("Welcome to ATM")

        else:

            print("\nInvalid User ID or PIN")


atm = ATMLogin()
atm.login()