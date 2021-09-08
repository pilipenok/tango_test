import sqlite3
from contextlib import closing
from typing import List

client = sqlite3.connect('bigtable.db', check_same_thread=False)


SQL_FILTERED_SUBSCRIBTIONS = """
    SELECT user_id
    FROM subscriptions
    WHERE subscriber_id=? AND user_id IN ({})
"""


def filtered_online_set(user_id: int, online_ids: List) -> List:
    with closing(client.cursor()) as db:
        print(f"user_id={user_id} online_ids={online_ids}")
        # sqlite does not support list binding
        sql = SQL_FILTERED_SUBSCRIBTIONS.format(','.join(map(str, online_ids)))
        print(sql)
        db.execute(sql, (user_id, ))
        rows = list(db.fetchall())
    return map(lambda x: x[0], rows)
