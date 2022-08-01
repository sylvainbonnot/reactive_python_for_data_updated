import reactivex as rx

rx.empty().subscribe(on_next=print, on_completed=lambda: print("Done!"))
