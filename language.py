def select_language():
    """Prompt user to choose a language before login."""
    print("\n=============================")
    print("  Select Language / மொழி தேர்வு")
    print("=============================")
    print("1. English")
    print("2. Tamil (தமிழ்)")
    choice = input("Enter choice (1/2): ").strip()
    return "ta" if choice == "2" else "en"
