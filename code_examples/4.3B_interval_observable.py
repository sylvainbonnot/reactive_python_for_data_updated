import reactivex as rx
from reactivex import operators as ops


# careful time is in seconds now, not ms !
rx.interval(1).pipe(ops.map(lambda i: f"{i} Mississippi")).subscribe(lambda s: print(s))

# Keep application alive until user presses a key
input("Press any key to quit")
