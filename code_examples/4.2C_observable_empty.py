import reactivex as rx

rx.empty().subscribe(on_next=lambda s: print(s), on_completed=lambda: print("Done!"))
