import reactivex as rx
from reactivex import operators as ops

rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.filter(lambda s: len(s) >= 5), ops.take(2)
).subscribe(print)
