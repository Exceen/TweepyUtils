from pkg_resources import Requirement, resource_filename

config_path = resource_filename(Requirement.parse('tweepyutils'), 'tweepyutils_accounts.json')

username = 'username'
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'
is_main_account = 'is_main_account'


def nonNullValue(value, fallback_value):
    if value == None:
        return fallback_value
    return value