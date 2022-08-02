import reactivex as rx
from reactivex import operators as ops
import os


def recursive_files_in_directory(folder):
    def emit_files_recursively(observer, scheduler):
        for root, directories, filenames in os.walk(folder):
            for directory in directories:
                observer.on_next(os.path.join(root, directory))
            for filename in filenames:
                observer.on_next(os.path.join(root, filename))

        observer.on_completed()

    return rx.create(emit_files_recursively)


recursive_files_in_directory("/Users/sylvain/Desktop/stuff/").pipe(
    ops.filter(lambda f: f.endswith(".txt"))
).subscribe(on_next=print, on_error=print)
