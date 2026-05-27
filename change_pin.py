<<<<<<< HEAD
from database import get_connection
from translations import get_text

def change_pin(account_number, lang="en"):
    t = lambda key, *a: get_text(lang, key, *a)
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT pin FROM accounts WHERE account_number=?", (account_number,))
    row = cur.fetchone()

    old_pin = input(t("enter_old_pin")).strip()
    if row["pin"] != old_pin:
        print(t("wrong_pin"))
        conn.close()
        return

    new_pin = input(t("enter_new_pin")).strip()
    if not new_pin.isdigit() or len(new_pin) != 4:
        print("PIN must be exactly 4 digits.")
        conn.close()
        return

    confirm = input(t("confirm_new_pin")).strip()
    if new_pin != confirm:
        print(t("pin_mismatch"))
        conn.close()
        return

    cur.execute("UPDATE accounts SET pin=? WHERE account_number=?", (new_pin, account_number))
    conn.commit()
    conn.close()
    print(t("pin_changed"))
=======
class ChangePin:

    def change_pin(self, current_pin):

        print("\n" + "=" * 40)
        print("CHANGE PIN")
        print("=" * 40)

        old_pin = input("Enter Old PIN: ")

        if old_pin == current_pin:

            new_pin = input("Enter New PIN: ")

            confirm_pin = input("Confirm New PIN: ")

            if new_pin == confirm_pin:

                print("PIN Changed Successfully")

                return new_pin

            else:

                print("PIN Does Not Match")

                return current_pin

        else:

            print("Incorrect Old PIN")

            return current_pin
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
