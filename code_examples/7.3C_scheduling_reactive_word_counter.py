# Schedules a reactive process that counts the words in a text file every three seconds,
# but only prints it as a dict if it has changed

import reactivex as rx
from reactivex import operators as ops
import re


def words_from_file(file_name):
    file = open(file_name)

    # parse, clean, and push words in text file
    return rx.from_(file).pipe(
        ops.flat_map(lambda s: rx.from_(s.split())),
        ops.map(lambda w: re.sub(r"[^\w]", "", w)),
        ops.filter(lambda w: w != ""),
        ops.map(lambda w: w.lower()),
    )


def word_counter(file_name):

    # count words using `group_by()`
    # tuple the word with the count
    return words_from_file(file_name).pipe(
        ops.group_by(lambda word: word),
        ops.flat_map(
            lambda grp: ops.count()(grp).pipe(ops.map(lambda ct: (grp.key, ct)))
        ),
    )


# composes the above word_counter() into a dict
def word_counter_as_dict(file_name):
    return word_counter(file_name).pipe(ops.to_dict(lambda t: t[0], lambda t: t[1]))


# Schedule to create a word count dict every three seconds an article
# But only re-print if text is edited and word counts change

article_file = "../resources/bbc_news_article.txt"

# create a dict every three seconds, but only push if it changed
rx.interval(3).pipe(
    ops.flat_map(lambda i: word_counter_as_dict(article_file)),
    ops.distinct_until_changed(),
).subscribe(print)

# Keep alive until user presses any key
input("Starting, press any key to quit\n")
