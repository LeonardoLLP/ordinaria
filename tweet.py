from time import time
from useraccount import UserAccount

class Tweet:
    def __init__(self, message: str, sender: UserAccount):
        assert len(message) <= 140
        self.time = time
        self.message = message
        self.sender = sender

    def __str__(self):
        return "{} tweeted: {}".format(self.sender.alias, self.message)

