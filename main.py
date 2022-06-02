from time import time

# Clases vacías para poder especificarlas en UserAccount
class Tweet:
    pass
class Email:
    pass
class UserAccount:
    pass



#! Ejercicio 1: UserAccount
class UserAccount:
    def __init__(self, alias: str, email: Email, tweets: list[Tweet], followers: list[UserAccount], timeline: list[Tweet]):
        self.alias = alias
        self.email = email
        self.tweets = tweets
        self.__followers = followers
        self.timeline = timeline

    def follow(self, other_user: UserAccount):
        other_user.__followers.append(self)

    def tweet(self, tweet: Tweet):
        self.tweets.append(tweet)
        for follower in self.followers:
            follower.timeline.append(tweet)



#! Ejercicio 2: Tweet y sus subclases
class Tweet:
    def __init__(self, message, sender):
        self.time = time()
        self.message = message
        self.sender = sender

class DirectMessage(Tweet):
    def __init__(self, message, sender, receiver):
        super().__init__(message, sender)
        self.receiver = receiver

