from google.cloud import bigtable
from google.cloud.bigtable import row_filters, row_set
import logging
import config
from typing import List
from random import randint


bigtable_client = bigtable.Client(project=config.gcp_project_id, admin=True)
bigtable_instance = bigtable_client.instance(config.gcp_bigtable_instance_id)
table = bigtable_instance.table('subscriptions')
CF = 'cf1'


def filtered_online_set(user_id: int, online_ids: List) -> List:
    logging.info(f"user_id={user_id} online_ids={online_ids}")

    if CF not in table.list_column_families():
        create_db()

    prefix = f"{user_id}#"
    row_set_ = row_set.RowSet()
    row_set_.add_row_range_with_prefix(prefix)
    row_set_.add_row_range_from_keys(
        start_key=f"{prefix}0000".encode(),
        end_key=f"{prefix}1000".encode()
    )

    row_filter = row_filters.FamilyNameRegexFilter("cf1.user_id".encode())

    rows = table.read_rows(row_set=row_set_, filter_=row_filter)

    ids = []
    for row in rows:
        id = row.cells['cf1']['user_id'][0].value.decode('utf-8')
        ids.append(id)

    return list(set(online_ids) & set(ids))


def create_db():
    logging.info(f"creating subscriptions...")

    table.column_family(CF).create()

    for id in range(1000):
        for _ in range(randint(1, 1000)):
            user_id = randint(1, 1000)

            row_key = f"{id}#{user_id}"
            row = table.direct_row(row_key)
            row.set_cell(CF, "subscriber_id", id)
            row.set_cell(CF, "user_id", user_id)

            row.commit()

    logging.info(f"Done.")
