<<<<<<< HEAD
TRANSLATIONS = {
    "en": {
        "welcome":          "Welcome to the ATM",
        "enter_account":    "Enter Account Number: ",
        "enter_pin":        "Enter PIN: ",
        "invalid_login":    "Invalid account number or PIN.",
        "account_locked":   "Your account is locked. Please contact support.",
        "login_success":    "Login successful. Welcome, {}!",
        "select_option":    "Select an option:",
        "balance":          "Check Balance",
        "deposit":          "Deposit",
        "withdraw":         "Withdraw",
        "change_pin":       "Change PIN",
        "statement":        "Mini Statement",
        "logout":           "Logout",
        "current_balance":  "Current Balance: ${:.2f}",
        "enter_amount":     "Enter amount: $",
        "deposit_success":  "Deposited ${:.2f} successfully.",
        "withdraw_success": "Withdrawn ${:.2f} successfully.",
        "insufficient":     "Insufficient funds.",
        "invalid_amount":   "Invalid amount. Please enter a positive number.",
        "enter_old_pin":    "Enter current PIN: ",
        "enter_new_pin":    "Enter new PIN (4 digits): ",
        "confirm_new_pin":  "Confirm new PIN: ",
        "pin_mismatch":     "PINs do not match. Try again.",
        "pin_changed":      "PIN changed successfully.",
        "wrong_pin":        "Incorrect current PIN.",
        "no_transactions":  "No transactions found.",
        "statement_header": "--- Mini Statement (Last 10) ---",
        "goodbye":          "Thank you for using our ATM. Goodbye!",
        "attempts_left":    "{} attempt(s) remaining.",
    },
    "ta": {
        "welcome":          "ATM-க்கு வரவேற்கிறோம்",
        "enter_account":    "கணக்கு எண் உள்ளிடவும்: ",
        "enter_pin":        "PIN உள்ளிடவும்: ",
        "invalid_login":    "தவறான கணக்கு எண் அல்லது PIN.",
        "account_locked":   "உங்கள் கணக்கு பூட்டப்பட்டுள்ளது. ஆதரவை தொடர்பு கொள்ளவும்.",
        "login_success":    "உள்நுழைவு வெற்றிகரமானது. வரவேற்கிறோம், {}!",
        "select_option":    "ஒரு விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
        "balance":          "இருப்பு பார்க்க",
        "deposit":          "டெபாசிட்",
        "withdraw":         "பணம் எடுக்க",
        "change_pin":       "PIN மாற்ற",
        "statement":        "சிறு அறிக்கை",
        "logout":           "வெளியேறு",
        "current_balance":  "தற்போதைய இருப்பு: ₹{:.2f}",
        "enter_amount":     "தொகை உள்ளிடவும்: ₹",
        "deposit_success":  "₹{:.2f} வெற்றிகரமாக டெபாசிட் செய்யப்பட்டது.",
        "withdraw_success": "₹{:.2f} வெற்றிகரமாக எடுக்கப்பட்டது.",
        "insufficient":     "போதுமான நிதி இல்லை.",
        "invalid_amount":   "தவறான தொகை.",
        "enter_old_pin":    "தற்போதைய PIN உள்ளிடவும்: ",
        "enter_new_pin":    "புதிய PIN (4 இலக்கம்): ",
        "confirm_new_pin":  "புதிய PIN உறுதிப்படுத்தவும்: ",
        "pin_mismatch":     "PIN பொருந்தவில்லை.",
        "pin_changed":      "PIN வெற்றிகரமாக மாற்றப்பட்டது.",
        "wrong_pin":        "தவறான தற்போதைய PIN.",
        "no_transactions":  "பரிவர்த்தனைகள் இல்லை.",
        "statement_header": "--- சிறு அறிக்கை (கடைசி 10) ---",
        "goodbye":          "நன்றி! விடை பெறுகிறோம்.",
        "attempts_left":    "{} முயற்சி(கள்) மீதமுள்ளன.",
    },
}

def get_text(lang, key, *args):
    text = TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)
    return text.format(*args) if args else text
=======
translations = {

    "english": {
        "welcome": "WELCOME TO ATM",
        "enter_user": "Enter User ID: ",
        "enter_pin": "Enter PIN: ",
        "success": "Login Successful",
        "invalid": "Invalid User ID or PIN"
    },

    "tamil": {
        "welcome": "ATM-க்கு வரவேற்கிறோம்",
        "enter_user": "பயனர் ஐடியை உள்ளிடவும்: ",
        "enter_pin": "PIN எண்ணை உள்ளிடவும்: ",
        "success": "உள்நுழைவு வெற்றி",
        "invalid": "தவறான பயனர் ஐடி அல்லது PIN"
    },

    "hindi": {
        "welcome": "एटीएम में आपका स्वागत है",
        "enter_user": "यूज़र आईडी दर्ज करें: ",
        "enter_pin": "पिन दर्ज करें: ",
        "success": "लॉगिन सफल",
        "invalid": "गलत यूज़र आईडी या पिन"
    }
}
>>>>>>> 9347a5d93bf86052ecc438037165a874bc4a57fa
