from time import time
from useraccount import UserAccount

class Tweet:
    def __init__(self, message: str, sender: UserAccount):
        assert len(message) <= 140
        self.time = time
        self.message = message
        self.sender = sender

    def print_tweet(self, message: str):
        return "{} {}: {}".format(self.sender.alias, message, self.message)

    def __str__(self):
       return self.print_tweet("tweeted")