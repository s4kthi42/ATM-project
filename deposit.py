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