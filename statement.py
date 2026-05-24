class Statement:

    def show_statement(self, transactions):

        print("\n" + "=" * 40)
        print("MINI STATEMENT")
        print("=" * 40)

        if len(transactions) == 0:

            print("No Transactions Found")

        else:

            for transaction in transactions:

                print(transaction)