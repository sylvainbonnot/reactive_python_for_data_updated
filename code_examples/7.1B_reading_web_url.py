import reactivex as rx
from reactivex import operators as ops

from urllib.request import urlopen


def read_request(link):
    f = urlopen(link)

    return rx.from_(f).pipe(ops.map(lambda s: s.decode("utf-8").strip()))


read_request("https://goo.gl/rIaDyM").subscribe(print)
