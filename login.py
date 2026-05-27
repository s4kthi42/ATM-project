<<<<<<< HEAD
from database import get_connection
from translations import get_text

MAX_ATTEMPTS = 3

def login(lang="en"):
    """Returns account_number on success, None on failure/lock."""
    t = lambda key, *a: get_text(lang, key, *a)
    conn = get_connection()
    cur  = conn.cursor()

    acc_num = input(t("enter_account")).strip()
    cur.execute("SELECT * FROM accounts WHERE account_number=?", (acc_num,))
    row = cur.fetchone()

    if not row:
        print(t("invalid_login"))
        conn.close()
        return None

    if row["is_locked"]:
        print(t("account_locked"))
        conn.close()
        return None

    pin = input(t("enter_pin")).strip()
    if row["pin"] == pin:
        cur.execute("UPDATE accounts SET failed_attempts=0 WHERE account_number=?", (acc_num,))
        conn.commit()
        conn.close()
        print(t("login_success", row["holder_name"]))
        return acc_num
    else:
        attempts = row["failed_attempts"] + 1
        remaining = MAX_ATTEMPTS - attempts
        if attempts >= MAX_ATTEMPTS:
            cur.execute("UPDATE accounts SET is_locked=1, failed_attempts=? WHERE account_number=?", (attempts, acc_num))
            conn.commit()
            conn.close()
            print(t("account_locked"))
            return None
        else:
            cur.execute("UPDATE accounts SET failed_attempts=? WHERE account_number=?", (attempts, acc_num))
            conn.commit()
            conn.close()
            print(t("invalid_login"))
            print(t("attempts_left", remaining))
            return None
=======
import getpass
from translations import translations


class ATMLogin:

    def __init__(self, language):

        self.user_id = "1234567890"
        self.pin = "123"

        self.lang = translations[language]

    def login(self):

        print("\n" + "=" * 40)
        print(self.lang["welcome"])
        print("=" * 40)

        entered_user_id = input(
            self.lang["enter_user"]
        )

        entered_pin = getpass.getpass(
            self.lang["enter_pin"]
        )

        if entered_user_id == self.user_id and entered_pin == self.pin:

            print("\n" + self.lang["success"])

            return True

        else:

            print("\n" + self.lang["invalid"])

            return False
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
