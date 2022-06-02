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



#! Respuestas al ejercicio 2.d

#? a) Si, en timeline solamente deberán aparecer los mensajes que no son DirectMessages.
#? Sin embargo, no hay que cambiar la variable tweets, ya que esa seguirá aceptando todos los tweets del propio user, sea un mensaje directo o no

#? No, ya que en python, si funciona con la clase madre, también funciona con la clase hija. Es un principio de diseño de la POO.


