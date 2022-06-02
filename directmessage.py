from tweet import Tweet
from useraccount import UserAccount

class DirectMessage(Tweet):
    def __init__(self, message: str, sender: UserAccount, receiver: UserAccount):
        super().__init__(message, sender)
        self.receiver = receiver