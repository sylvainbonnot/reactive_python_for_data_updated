from reactivex import Observable, create
import reactivex as rx


def push_numbers(
    observer, scheduler=None
):  # create takes now a scheduler as second parameter
    observer.on_next(300)
    observer.on_next(450)
    observer.on_next(700)
    observer.on_completed()


# rx.of(push_numbers).subscribe(lambda i:print(i))
create(push_numbers).subscribe(lambda i: print(i))
