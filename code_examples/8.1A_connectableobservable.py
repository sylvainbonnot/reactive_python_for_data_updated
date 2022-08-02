import reactivex as rx
from reactivex import operators as ops

source = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]).pipe(ops.publish())

source.subscribe(lambda s: print(f"Subscriber 1: {s}"))
source.subscribe(lambda s: print(f"Subscriber 2: {0}"))

source.connect()
