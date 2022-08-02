import reactivex as rx
from reactivex import operators as ops
import time
from reactivex.scheduler import ThreadPoolScheduler
from threading import current_thread
import multiprocessing, time, random


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * 0.1)
    return value


# calculate number of CPU's and add 1, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

# Create Parallel Process
rx.from_(
    [
        "Alpha",
        "Beta",
        "Gamma",
        "Delta",
        "Epsilon",
        "Zeta",
        "Eta",
        "Theta",
        "Iota",
        "Kappa",
    ]
).pipe(
    ops.flat_map(
        lambda s: rx.just(s).pipe(
            ops.subscribe_on(pool_scheduler), ops.map(lambda s: intense_calculation(s))
        )
    )
).subscribe(
    on_next=lambda i: print("{0} {1}".format(current_thread().name, i)),
    on_error=lambda e: print(e),
    on_completed=lambda: print("PROCESS 1 done!"),
)


input("Press any key to exit\n")
