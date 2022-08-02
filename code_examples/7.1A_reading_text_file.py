import reactivex as rx
from reactivex import operators as ops


def read_lines(file_name):
    file = open(file_name)

    return rx.from_(file).pipe(
        ops.map(lambda l: l.strip()), ops.filter(lambda l: l != "")
    )


read_lines("../resources/bbc_news_article.txt").subscribe(print)
