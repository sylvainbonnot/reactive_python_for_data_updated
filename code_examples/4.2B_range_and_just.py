import reactivex as rx

# Using Observable.range()
letters = rx.range(1, 10)
letters.subscribe(print)

# Using Observable.just()
greeting = rx.just("Hello World!")
greeting.subscribe(print)
