import helper
from account import Account
import json

accounts = {}

def init_accounts():
    global accounts
    global _config
    with open(helper.config_path, 'r') as f:
        config = json.load(f)
        for key, data in config.iteritems():
            consumer_key = data.get(helper.consumer_key)
            consumer_secret = data.get(helper.consumer_secret)
            access_token = data.get(helper.access_token)
            access_token_secret = data.get(helper.access_token_secret)
            is_main_account = helper.nonNullValue(data.get(helper.is_main_account), False)

            account = Account('Exceen', is_main_account, consumer_key, consumer_secret, access_token, access_token_secret)
            accounts[key] = account

def get_main_account():
    return __get_account(True)

def get_secondary_account():
    return __get_account(False)

def __get_account(is_main_account):
    for key in accounts:
        if accounts[key].is_main_account == is_main_account:
            return accounts[key]
    return None    

init_accounts()