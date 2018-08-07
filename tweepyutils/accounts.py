import helper
from account import Account
import json
import os.path

_accounts = {}

def __init_accounts():
    global accounts
    global _config

    if os.path.isfile(helper.config_path):
        with open(helper.config_path, 'r') as f:
            config = json.load(f)
            for key, data in config.iteritems():
                consumer_key = data.get(helper.consumer_key)
                consumer_secret = data.get(helper.consumer_secret)
                access_token = data.get(helper.access_token)
                access_token_secret = data.get(helper.access_token_secret)
                is_main_account = data.get(helper.is_main_account) or False

                account = Account(consumer_key, consumer_secret, access_token, access_token_secret, is_main_account)
                _accounts[key] = account

def get_main_account():
    return __get_account(True)

def get_secondary_account():
    return __get_account(False)

def get_account(name):
    return _accounts[name]

def get_available_accounts():
    return _accounts.keys()

def __get_account(is_main_account):
    for key, account in _accounts.iteritems():
        if account.is_main_account == is_main_account:
            return account
    return None    

def get_api(name):
    return get_account(name).api


__init_accounts()

