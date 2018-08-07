import tweepy

class Account(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, is_main_account=False):
        super(Account, self).__init__()

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.is_main_account = is_main_account

        self._api = None

    @property
    def api(self):
        if self._api is None:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)
            self._api = tweepy.API(auth)
        return self._api

    @api.setter
    def api(self, api):
        self._api = api

    @api.deleter
    def api(self):
        del self._api
