import reactivex as rx
from reactivex import operators as ops
import time

source = rx.interval(1).pipe(ops.publish())

source.subscribe(lambda s: print(f"Subscriber 1: {s}"))
source.connect()

# sleep 5 seconds, then add another subscriber
time.sleep(5)
source.subscribe(lambda s: print(f"Subscriber 2: {s}"))

input("Press any key to exit\n")
