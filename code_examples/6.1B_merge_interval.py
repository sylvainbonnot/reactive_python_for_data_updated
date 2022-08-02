import reactivex as rx
from reactivex import operators as ops


source1 = rx.interval(1).pipe(ops.map(lambda i: f"Source 1: {i}"))
source2 = rx.interval(5).pipe(ops.map(lambda i: f"Source 2: {i}"))
source3 = rx.interval(3).pipe(ops.map(lambda i: f"Source 3: {i}"))

rx.merge(source1, source2, source3).subscribe(print)

# keep application alive until user presses a key
input("Press any key to quit\n")
