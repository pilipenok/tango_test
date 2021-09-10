from google.cloud import bigtable
from google.cloud.bigtable import row_filters, row_set
import config
from typing import List
from random import randint
import datetime


bigtable_client = bigtable.Client(project=config.gcp_project_id, admin=True)
bigtable_instance = bigtable_client.instance(config.gcp_bigtable_instance_id)
table = bigtable_instance.table('subscriptions')
CF = 'cf1'


def filtered_online_set(user_id: int, online_ids: List) -> List:
    print(f"user_id={user_id} online_ids={online_ids}")

    if CF not in table.list_column_families():
        create_db()

    prefix = f"{user_id}#"
    row_set_ = row_set.RowSet()
    row_set_.add_row_range_with_prefix(prefix)
    row_set_.add_row_range_from_keys(
        start_key=f"{prefix}0000".encode(),
        end_key=f"{prefix}1000".encode()
    )

    row_filter = row_filters.ColumnQualifierRegexFilter(b"user_id")

    rows = table.read_rows(row_set=row_set_, filter_=row_filter)

    ids = []
    for row in rows:
        id = row.cells['cf1'][b'user_id'][0].value.decode('utf-8')
        ids.append(id)
    #return ids

    return [id for id in ids if id in online_ids]
    # return list(set(online_ids) & set(ids))


def create_db():
    print(f"creating subscriptions...")

    table.column_family(CF).create()

    rows = []
    for id in range(1000):
        print(f'id={id}')
        for _ in range(randint(1, 100)):
            user_id = randint(1, 1000)
            row_key = f"{id}#{user_id}".encode()
            row = table.direct_row(row_key)
            row.set_cell(CF, b"subscriber_id", str(id), timestamp=datetime.datetime.utcnow())
            row.set_cell(CF, b"user_id", str(user_id), timestamp=datetime.datetime.utcnow())
            rows.append(row)
            if len(rows) == 10000:
                table.mutate_rows(rows)
                rows = []

    if len(rows) > 0:
        table.mutate_rows(rows)
    print(f"Done.")
