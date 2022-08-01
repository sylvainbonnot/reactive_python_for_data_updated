import reactivex as rx
from reactivex import operators as ops

rx.from_([2, 5, 21, 5, 2, 1, 5, 63, 127, 12]).pipe(
    ops.take_while(lambda i: i < 100)
).subscribe(on_next=print, on_completed=lambda: print("Done!"))
