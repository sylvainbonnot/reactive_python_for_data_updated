import reactivex as rx
from reactivex import operators as ops

items = ["134/34/235/132/77", "64/22/98/112/86/11", "66/08/34/778/22/12"]

rx.from_(items).pipe(
    ops.flat_map(lambda s: rx.from_(s.split("/"))), ops.map(int)
).subscribe(print)
