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
