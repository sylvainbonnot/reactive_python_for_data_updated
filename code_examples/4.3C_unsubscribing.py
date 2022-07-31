import reactivex as rx
import time
from reactivex import operators as ops


disposable = (
    rx.interval(1)
    .pipe(ops.map(lambda i: f"{i} Mississippi"))
    .subscribe(lambda s: print(s))
)

# sleep 5 seconds so Observable can fire
time.sleep(5)

# disconnect the Subscriber
print("Unsubscribing!")
disposable.dispose()

# sleep a bit longer to prove no more emissions are coming
time.sleep(5)
