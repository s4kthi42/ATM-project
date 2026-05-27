<<<<<<< HEAD
from database import get_connection
from translations import get_text

def deposit(account_number, lang="en"):
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
    new_balance = round(row["balance"] + amount, 2)

    cur.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, account_number))
    cur.execute(
        "INSERT INTO transactions(account_number,type,amount,balance_after,note) VALUES(?,?,?,?,?)",
        (account_number, "DEPOSIT", amount, new_balance, "Customer deposit")
    )
    conn.commit()
    conn.close()
    print(t("deposit_success", amount))
    print(t("current_balance", new_balance))
=======
class Deposit:

    def deposit_money(self, balance, transactions):

        print("\n" + "=" * 40)
        print("DEPOSIT MONEY")
        print("=" * 40)

        amount = float(input("Enter Deposit Amount: ₹"))

        balance += amount

        transactions.append(f"Deposited ₹{amount}")

        print("Amount Deposited Successfully")
        print(f"Updated Balance: ₹{balance}")

        return balance
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
