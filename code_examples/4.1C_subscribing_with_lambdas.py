import reactivex as rx

letters = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])

letters.subscribe(
    on_next=lambda value: print(value),
    on_completed=lambda: print("Completed!"),
    on_error=lambda error: print(f"Error occurred: {error}"),
)

# to use just on_next:
# letters.subscribe(on_next = lambda value: print(value))
# letters.subscribe(lambda value: print(f'Received: {error}'))
