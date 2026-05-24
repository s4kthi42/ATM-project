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