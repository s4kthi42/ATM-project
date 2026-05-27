import sqlite3
import random
from datetime import datetime, timedelta

DB_FILE = "atm_database.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def _random_name():
    first = ["Aarav","Aditi","Aisha","Ajay","Akash","Amar","Amit","Ananya","Anil","Anjali",
             "Ankit","Arjun","Aruna","Ashok","Bala","Bharat","Chandra","Deepa","Deepak","Divya",
             "Ganesh","Geeta","Harish","Harsha","Hema","Isha","Ishaan","Jagdish","Jaya","Karan",
             "Kavita","Keerthana","Kishore","Komal","Krishna","Kumar","Lakshmi","Lavanya","Madhu",
             "Mahesh","Manish","Meena","Mohan","Monica","Mukesh","Nandini","Naveen","Neha","Nikhil",
             "Nisha","Nithya","Pavan","Pooja","Pradeep","Prakash","Priya","Rahul","Rajesh","Ramesh",
             "Ranjith","Ravi","Rekha","Rohit","Roshan","Sachin","Sanjay","Sara","Saravanan","Sathish",
             "Seema","Shankar","Shilpa","Shivam","Shruti","Sneha","Soham","Sridhar","Suresh","Sushma",
             "Swathi","Tanvi","Tarun","Uday","Uma","Usha","Varun","Venkat","Vijay","Vikram","Vinod",
             "Vivek","Yamini","Riya","Tara","Sia","Mia","Jai","Dev","Raj","Nia"]
    last  = ["Agarwal","Bhatt","Chauhan","Das","Desai","Dubey","Gandhi","Ghosh","Gupta","Iyer",
             "Jain","Joshi","Kapoor","Kaur","Khan","Khanna","Kumar","Lal","Malhotra","Mehta",
             "Mishra","Mukherjee","Nair","Naidu","Pandey","Patel","Patil","Pillai","Raj","Rao",
             "Reddy","Saha","Sharma","Shukla","Singh","Sinha","Srinivasan","Subramanian","Tiwari",
             "Tripathi","Varma","Verma","Yadav","Fernandes","Chowdhury","Goswami","Devi","Bajaj","Bose"]
    return f"{random.choice(first)} {random.choice(last)}"

def _random_pin():
    return f"{random.randint(1000,9999)}"

def _random_balance():
    return round(random.uniform(500.0, 150000.0), 2)

def _random_acc(existing):
    while True:
        num = f"10{random.randint(10000000,99999999)}"
        if num not in existing:
            existing.add(num)
            return num

def initialize_db():
    conn = get_connection()
    cur  = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number  TEXT    PRIMARY KEY,
            pin             TEXT    NOT NULL,
            holder_name     TEXT    NOT NULL,
            balance         REAL    DEFAULT 0.0,
            language        TEXT    DEFAULT 'en',
            is_locked       INTEGER DEFAULT 0,
            failed_attempts INTEGER DEFAULT 0,
            created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number TEXT    NOT NULL,
            type           TEXT    NOT NULL,
            amount         REAL    NOT NULL,
            balance_after  REAL    NOT NULL,
            timestamp      DATETIME DEFAULT CURRENT_TIMESTAMP,
            note           TEXT,
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
        )
    """)

    cur.execute("SELECT COUNT(*) FROM accounts")
    if cur.fetchone()[0] == 0:
        print("[DB] Seeding 1000 accounts ...")
        existing = set()

        demo = [
            ("1001111111","1234","Alice Johnson",  25000.00,"en"),
            ("1002222222","5678","Bob Smith",       12500.50,"en"),
            ("1003333333","0000","Tamil Arasan",     8200.75,"ta"),
        ]
        for d in demo:
            existing.add(d[0])
        cur.executemany(
            "INSERT INTO accounts(account_number,pin,holder_name,balance,language) VALUES(?,?,?,?,?)",
            demo
        )

        rand_accs = []
        for _ in range(997):
            num  = _random_acc(existing)
            pin  = _random_pin()
            name = _random_name()
            bal  = _random_balance()
            lang = random.choice(["en","en","en","ta"])
            rand_accs.append((num,pin,name,bal,lang))
        cur.executemany(
            "INSERT INTO accounts(account_number,pin,holder_name,balance,language) VALUES(?,?,?,?,?)",
            rand_accs
        )

        print("[DB] Seeding transactions ...")
        all_accs  = list(demo) + rand_accs
        txn_batch = []
        base_time = datetime.now() - timedelta(days=180)

        for acc in all_accs:
            acc_num     = acc[0]
            running_bal = acc[3]
            for _ in range(random.randint(3, 8)):
                txn_type = random.choice(["DEPOSIT","WITHDRAW","DEPOSIT","DEPOSIT","WITHDRAW"])
                amount   = round(random.uniform(100, 5000), 2)
                if txn_type == "WITHDRAW":
                    if amount > running_bal:
                        amount = round(running_bal * 0.3, 2)
                    if amount < 10:
                        txn_type = "DEPOSIT"
                        amount   = round(random.uniform(500, 5000), 2)
                running_bal = round(running_bal + amount if txn_type == "DEPOSIT" else running_bal - amount, 2)
                ts = base_time + timedelta(days=random.randint(0,179), hours=random.randint(0,23), minutes=random.randint(0,59))
                txn_batch.append((acc_num, txn_type, amount, running_bal, ts.strftime("%Y-%m-%d %H:%M:%S"), f"Seeded {txn_type.lower()}"))

        cur.executemany(
            "INSERT INTO transactions(account_number,type,amount,balance_after,timestamp,note) VALUES(?,?,?,?,?,?)",
            txn_batch
        )
        conn.commit()

        cur.execute("SELECT COUNT(*) FROM accounts")
        a = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM transactions")
        t = cur.fetchone()[0]
        print(f"[DB] Done: {a} accounts, {t} transactions.")
    else:
        print("[DB] Database already initialised.")

    conn.close()
