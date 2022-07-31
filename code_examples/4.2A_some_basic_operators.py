import reactivex as rx
from reactivex import operators as ops

letters = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
letters.pipe(ops.map(lambda s: len(s)), ops.filter(lambda i: i >= 5)).subscribe(
    lambda value: print("Received {0}".format(value))
)
