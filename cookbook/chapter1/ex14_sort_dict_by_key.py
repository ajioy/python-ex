rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# itemgetter和lambda效果一样，但是效率高些
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_id = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_id)

rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

rows_by_uid = sorted(rows, key=lambda r:r['uid'])
rows_by_lname = sorted(rows, key=lambda r:(r['lname'],r['fname']))
print(rows_by_fname)
print(rows_by_lname)

min_row = min(rows, key=itemgetter('uid'))
print(min_row)
max_row = max(rows, key=itemgetter('uid'))
print(max_row)
