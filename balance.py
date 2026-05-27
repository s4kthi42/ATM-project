<<<<<<< HEAD
from database import get_connection
from translations import get_text

def check_balance(account_number, lang="en"):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE account_number=?", (account_number,))
    row = cur.fetchone()
    conn.close()
    if row:
        print(get_text(lang, "current_balance", row["balance"]))
    
def get_balance(account_number):
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE account_number=?", (account_number,))
    row = cur.fetchone()
    conn.close()
    return row["balance"] if row else 0.0
=======
class Balance:

    def check_balance(self, balance):

        print("\n" + "=" * 40)
        print("CHECK BALANCE")
        print("=" * 40)

        print(f"Available Balance: ₹{balance}")
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
