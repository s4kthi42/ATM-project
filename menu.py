<<<<<<< HEAD
from translations import get_text
from balance   import check_balance
from deposit   import deposit
from withdraw  import withdraw
from change_pin import change_pin
from statement import mini_statement

def show_menu(account_number, lang="en"):
    t = lambda key, *a: get_text(lang, key, *a)
    while True:
        print("\n" + "="*35)
        print(f"  {t('select_option')}")
        print("="*35)
        print(f"  1. {t('balance')}")
        print(f"  2. {t('deposit')}")
        print(f"  3. {t('withdraw')}")
        print(f"  4. {t('change_pin')}")
        print(f"  5. {t('statement')}")
        print(f"  6. {t('logout')}")
        print("="*35)

        choice = input("  > ").strip()
        if   choice == "1": check_balance(account_number, lang)
        elif choice == "2": deposit(account_number, lang)
        elif choice == "3": withdraw(account_number, lang)
        elif choice == "4": change_pin(account_number, lang)
        elif choice == "5": mini_statement(account_number, lang)
        elif choice == "6":
            print(t("goodbye"))
            break
        else:
            print("Invalid choice. Try again.")
=======
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
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
