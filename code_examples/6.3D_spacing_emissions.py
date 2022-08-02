import reactivex as rx
from reactivex import operators as ops

letters = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
intervals = rx.interval(1)

rx.zip(letters, intervals).pipe(ops.map(lambda item: item[0])).subscribe(print)

input("Press any key to quit\n")
