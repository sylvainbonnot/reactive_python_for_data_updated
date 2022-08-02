import reactivex as rx
from reactivex import operators as ops

rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.to_dict(lambda s: s[0])
).subscribe(print)

rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(
    ops.to_dict(lambda s: s[0], lambda s: len(s))
).subscribe(print)
