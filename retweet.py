from tweet import Tweet
from useraccount import UserAccount

class Retweet(Tweet):
    def __init__(self, message: str, sender: UserAccount, original_tweet: Tweet):
        super().__init__(message, sender)
        self.original_tweet = original_tweet