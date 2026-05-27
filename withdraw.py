from database import get_connection
from translations import get_text

def withdraw(account_number, lang="en"):
    t = lambda key, *a: get_text(lang, key, *a)
    try:
        amount = float(input(t("enter_amount")))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print(t("invalid_amount"))
        return

    conn = get_connection()
    cur  = conn.cursor()
    cur.execute("SELECT balance FROM accounts WHERE account_number=?", (account_number,))
    row = cur.fetchone()

    if row["balance"] < amount:
        print(t("insufficient"))
        conn.close()
        return

    new_balance = round(row["balance"] - amount, 2)
    cur.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, account_number))
    cur.execute(
        "INSERT INTO transactions(account_number,type,amount,balance_after,note) VALUES(?,?,?,?,?)",
        (account_number, "WITHDRAW", amount, new_balance, "Customer withdrawal")
    )
    conn.commit()
    conn.close()
    print(t("withdraw_success", amount))
    print(t("current_balance", new_balance))
