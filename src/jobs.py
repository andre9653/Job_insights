import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        reader_path = csv.DictReader(file)
        list_rows = []
        for row in reader_path:
            list_rows.append(row)
    return list_rows
