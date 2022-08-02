import reactivex as rx
from reactivex import operators as ops

letters = rx.from_(["A", "B", "C", "D", "E", "F"])
numbers = rx.range(1, 5)

rx.zip(letters, numbers).pipe(ops.map(lambda item: f"{item[0]}-{item[1]}")).subscribe(
    print
)
