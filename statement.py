from database import get_connection
from translations import get_text

def mini_statement(account_number, lang="en"):
    t = lambda key, *a: get_text(lang, key, *a)
    conn = get_connection()
    cur  = conn.cursor()
    cur.execute(
        "SELECT type,amount,balance_after,timestamp FROM transactions "
        "WHERE account_number=? ORDER BY timestamp DESC LIMIT 10",
        (account_number,)
    )
    rows = cur.fetchall()
    conn.close()

    print(t("statement_header"))
    if not rows:
        print(t("no_transactions"))
        return
    print(f"{'Date':<20} {'Type':<10} {'Amount':>12} {'Balance':>12}")
    print("-" * 58)
    for r in rows:
        print(f"{r['timestamp']:<20} {r['type']:<10} {r['amount']:>12.2f} {r['balance_after']:>12.2f}")
