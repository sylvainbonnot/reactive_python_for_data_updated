import reactivex as rx

words = rx.from_(["Mary", "had", "a", "little", "lamb"])
words.subscribe(print)
