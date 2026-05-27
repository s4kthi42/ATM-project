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
