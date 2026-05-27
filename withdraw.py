<<<<<<< HEAD
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
=======
class Withdraw:

    def withdraw_money(self, balance, transactions):

        print("\n" + "=" * 40)
        print("WITHDRAW MONEY")
        print("=" * 40)

        amount = float(input("Enter Withdraw Amount: ₹"))

        if amount <= balance:

            balance -= amount

            transactions.append(f"Withdrawn ₹{amount}")

            print("Please Collect Your Cash")
            print(f"Remaining Balance: ₹{balance}")

        else:

            print("Insufficient Balance")

        return balance  
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
