# from tweepy.streaming import StreamListener
# from tweepy import OAuthHandler
# from tweepy import Stream
import json
import reactivex as rx
from reactivex import operators as ops
import tweepy


def tweets_for(topics):
    def observe_tweets(observer, scheduler):
        class TweetListener(tweepy.Stream):
            def on_data(self, data):
                observer.on_next(data)
                return True

            def on_error(self, status):
                observer.on_error(status)

        # This handles Twitter authetification and the connection to Twitter Streaming API
        # l = TweetListener()
        # client = tweepy.Client(
        #    consumer_key, consumer_secret, access_token, access_token_secret
        # )

        stream = TweetListener(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        # auth = OAuthHandler(consumer_key, consumer_secret)
        # auth.set_access_token(access_token, access_token_secret)
        # stream = TweetListener(client)
        # stream = tweepy.StreamingClient(bearer_token)
        # stream = Stream(auth, l)
        stream.filter(track=topics)

    return rx.create(observe_tweets).pipe(ops.share())


topics = ["Britain"]

tweets_for(topics).pipe(
    ops.map(lambda d: json.loads(d)),
    ops.filter(lambda map: "text" in map),
    ops.map(lambda map: map["text"].strip()),
).subscribe(lambda s: print(s))
