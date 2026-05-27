<<<<<<< HEAD
"""
ATM System - Main Entry Point
==============================
Demo Accounts:
  Account: 1001111111  PIN: 1234  (English)
  Account: 1002222222  PIN: 5678  (English)
  Account: 1003333333  PIN: 0000  (Tamil)

Database: SQLite (atm_database.db)
  - 1000 accounts pre-seeded
  - ~5000 transaction records
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database     import initialize_db
from language     import select_language
from login        import login
from menu         import show_menu

def main():
    print("\n" + "="*35)
    print("       WELCOME TO PYTHON ATM")
    print("="*35)

    initialize_db()

    while True:
        lang        = select_language()
        account_num = login(lang)
        if account_num:
            show_menu(account_num, lang)

        again = input("\nUse ATM again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!\n")
            break

if __name__ == "__main__":
    main()
=======
import os

os.system("chcp 65001")

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
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
