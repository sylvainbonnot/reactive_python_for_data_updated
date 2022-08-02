import tweepy

bearer_token = "TOKEN_HERE"

# client = tweepy.Client(bearer_token=bearer_token)

# Replace with your own search query
# query = "from:suhemparack -is:retweet"
# query = "from:sylvainbonnot -is:retweet"
class IDPrinter(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.id)


printer = IDPrinter(bearer_token=bearer_token)
printer.add_rules(tweepy.StreamRule("France"))
printer.filter()
# printer.sample()

# tweets = client.search_recent_tweets(
#     query=query, tweet_fields=["context_annotations", "created_at"], max_results=10
# )

# for tweet in tweets.data:
#     print(tweet.text)
#     if len(tweet.context_annotations) > 0:
#         print(tweet.context_annotations)
