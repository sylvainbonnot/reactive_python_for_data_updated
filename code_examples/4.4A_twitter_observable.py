import reactivex as rx
from reactivex import operators as ops
import tweepy

# Variables that contains the user credentials to access Twitter API
bearer_token = "INSERT_TOKEN_HERE"


def tweets_for(topics):
    def observe_tweets(observer, scheduler):
        class TweetListener(tweepy.StreamingClient):
            def on_tweet(self, tweet):
                observer.on_next(tweet)
                return True

            def on_error(self, status):
                observer.on_error(status)

        stream = TweetListener(bearer_token=bearer_token)
        stream.add_rules(tweepy.StreamRule(*topics))

        stream.filter()

    return rx.create(observe_tweets).pipe(ops.share())


topics = ["Britain", "France"]

tweets_for(topics).pipe(
    ops.filter(lambda map: "text" in map),
    ops.map(lambda map: map["text"].strip()),
).subscribe(print)
