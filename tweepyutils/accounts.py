import constants
import tweepy

def get_available_account_names():
    return constants.config.account_config.keys()


def get_account(name):
    return constants.config.account_config[name]


def get_main_account():
    return __get_account(True)

def get_secondary_account():
    return __get_account(False)

def __get_account(is_main_account):
    for key, account in constants.config.account_config.iteritems():
        if account.is_main_account == is_main_account:
            return account
    return None   


def get_api(name):
    return get_account(name).api

def config_contains_account(name):
    return name in constants.config.account_config

def add_account_to_config(key, account):
    constants.config.account_config[key] = account
    constants.config.save()

def remove_account_from_config(key):
    constants.config.account_config.pop(key, None)
    constants.config.save()

class Account(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, is_main_account=False):
        super(Account, self).__init__()

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.is_main_account = is_main_account

        self._api = None
        
        self._friends = None
        self._followers = None

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
        
        
    @property
    def friends(self):
        if self._friends is None:
            self._friends = [str(friend) for friend in self.api.friends_ids(self.api.me().screen_name)]
        return self._friends
    
    @friends.setter
    def friends(self, friends):
        self._friends = friends

    @friends.deleter
    def friends(self):
        del self._friends    
    
    
    @property
    def followers(self):
        if self._followers is None:
            self._followers = [str(follower) for follower in self.api.followers_ids(self.api.me().screen_name)]
        return self._followers
    
    @followers.setter
    def followers(self, followers):
        self._followers = followers

    @followers.deleter
    def followers(self):
        del self._followers

    def to_json(self):
        json_account = {}
        json_account[constants.CONSUMER_KEY] = self.consumer_key
        json_account[constants.CONSUMER_SECRET] = self.consumer_secret
        json_account[constants.ACCESS_TOKEN] = self.access_token
        json_account[constants.ACCESS_TOKEN_SECRET] = self.access_token_secret

        if self.is_main_account:
            json_account[constants.IS_MAIN_ACCOUNT] = self.is_main_account
            
        return json_account


