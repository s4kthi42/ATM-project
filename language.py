class Language:

    def choose_language(self):

        print("1. English")
        print("2. Tamil")
        print("3. Hindi")

        choice = input("Choose Language: ")

        if choice == "1":
            return "english"

        elif choice == "2":
            return "tamil"

        elif choice == "3":
            return "hindi"

        else:
            print("Invalid Choice")
            return "english"