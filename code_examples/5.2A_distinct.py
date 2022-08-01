import reactivex as rx
from reactivex import operators as ops

rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.map(lambda s: len(s)), ops.distinct()
).subscribe(print)
