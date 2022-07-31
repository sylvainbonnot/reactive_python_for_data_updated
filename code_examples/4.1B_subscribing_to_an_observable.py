import reactivex as rx
from reactivex import Observer

letters = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])


class MySubscriber(Observer):
    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("Completed!")

    def on_error(self, error):
        print("Error occured: {0}".format(error))


letters.subscribe(MySubscriber())
