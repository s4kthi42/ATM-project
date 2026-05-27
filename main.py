"""
ATM System - Main Entry Point
==============================
Demo Accounts:
  Account: 1001111111  PIN: 1234  (English)
  Account: 1002222222  PIN: 5678  (English)
  Account: 1003333333  PIN: 0000  (Tamil)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from database  import initialize_db
from language  import select_language
from login     import login
from menu      import show_menu

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
