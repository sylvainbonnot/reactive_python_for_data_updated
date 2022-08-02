import reactivex as rx
from reactivex import operators as ops


rx.from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.map(lambda s: len(s)), ops.distinct_until_changed()
).subscribe(print)


rx.from_(["Alpha", "Theta", "Kappa", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.distinct_until_changed(lambda s: len(s))
).subscribe(print)
