from time import time
from useraccount import UserAccount
class Tweet:
    def __init__(self, message: str, sender: UserAccount):
        assert len(message) <= 140
        self.time = time
        self.message = message
        self.sender = sender

    def __str__(self):
        return self.message

class DirectMessage(Tweet):
    def __init__(self, message: str, sender: UserAccount, receiver: UserAccount):
        super().__init__(message, sender)
        self.receiver = receiver

class Retweet(Tweet):
    def __init__(self, message: str, sender: UserAccount, original_tweet: Tweet):
        super().__init__(message, sender)
        self.original_tweet = original_tweet