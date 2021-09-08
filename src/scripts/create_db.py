import sqlite3
from random import randint
if __name__ == '__main__':
    conn = sqlite3.connect('bigtable.db', check_same_thread=False)

    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS subscriptions(subscriber_id INTEGER, user_id INTEGER , created_at DATETIME)
    """)

    for id in range(1000):
        for _ in range(randint(1, 1000)):
            user_id = randint(1, 1000)
            conn.execute("INSERT INTO subscriptions values(?,?,CURRENT_TIMESTAMP)", (id, user_id,))

    conn.commit()
    conn.close()