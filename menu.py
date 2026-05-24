from balance import Balance
from deposit import Deposit
from withdraw import Withdraw
from statement import Statement
from change_pin import ChangePin


class ATMMenu:

    def show_menu(self):

        balance = 5000

        pin = "123"

        transactions = []

        # Object Creation
        balance_obj = Balance()
        deposit_obj = Deposit()
        withdraw_obj = Withdraw()
        statement_obj = Statement()
        change_pin_obj = ChangePin()

        while True:

            print("\n" + "=" * 40)
            print("ATM MAIN MENU")
            print("=" * 40)

            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            # Check Balance
            if choice == "1":

                balance_obj.check_balance(balance)

            # Deposit Money
            elif choice == "2":

                balance = deposit_obj.deposit_money(
                    balance,
                    transactions
                )

            # Withdraw Money
            elif choice == "3":

                balance = withdraw_obj.withdraw_money(
                    balance,
                    transactions
                )

            # Mini Statement
            elif choice == "4":

                statement_obj.show_statement(
                    transactions
                )

            # Change PIN
            elif choice == "5":

                pin = change_pin_obj.change_pin(pin)

            # Exit
            elif choice == "6":

                print("\nThank You For Using ATM")
                break

            # Invalid Choice
            else:

                print("\nInvalid Choice")