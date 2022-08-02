import reactivex as rx
from reactivex import operators as ops

items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]

rx.from_(items).pipe(
    ops.group_by(lambda s: len(s)), ops.flat_map(lambda grp: ops.to_list()(grp))
).subscribe(print)
