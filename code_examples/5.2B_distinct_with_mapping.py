import reactivex as rx
from reactivex import operators as ops

rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.distinct(lambda s: len(s))
).subscribe(print)
