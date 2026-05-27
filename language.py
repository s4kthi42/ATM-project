<<<<<<< HEAD
def select_language():
    """Prompt user to choose a language before login."""
    print("\n=============================")
    print("  Select Language / மொழி தேர்வு")
    print("=============================")
    print("1. English")
    print("2. Tamil (தமிழ்)")
    choice = input("Enter choice (1/2): ").strip()
    return "ta" if choice == "2" else "en"
=======
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
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
