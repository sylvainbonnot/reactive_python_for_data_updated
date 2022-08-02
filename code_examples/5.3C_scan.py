import reactivex as rx
from reactivex import operators as ops

rx.from_([4, 76, 22, 66, 881, 13, 35]).pipe(
    ops.scan(lambda total, value: total + value)
).subscribe(print)
