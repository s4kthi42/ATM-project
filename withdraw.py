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