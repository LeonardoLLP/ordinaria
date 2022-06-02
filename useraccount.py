class Tweet:
    pass
class Email:
    pass
class UserAccount:
    pass

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
        for follower in self.__followers:
            follower.timeline.append(tweet)