import reactivex as rx
from reactivex import operators as ops


items = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]


rx.from_(items).pipe(
    ops.group_by(lambda l: len(l)),
    ops.flat_map(lambda grp: ops.count()(grp).pipe(ops.map(lambda ct: (grp.key, ct)))),
    ops.to_dict(lambda t: t[0], lambda t: t[1]),
).subscribe(print)
