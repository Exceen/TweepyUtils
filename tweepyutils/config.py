import json
import os
from . import constants
from . import accounts

class Config(object):
    def __init__(self, config_file):
        super(Config, self).__init__()

        self.config_file = config_file
        self._config = None

    @property
    def config(self):
        if self._config == None:
            self.__init_config()
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    @config.deleter
    def config(self):
        self._config = {}


    @property
    def account_config(self):
        if constants.ACCOUNTS not in self.config:
            self.config[constants.ACCOUNTS] = {}
        return self.config[constants.ACCOUNTS]

    @account_config.setter
    def account_config(self, account_config):
        self.config[constants.ACCOUNTS] = account_config

    @account_config.deleter
    def account_config(self):
        self.config[constants.ACCOUNTS] = {}



    def __init_config(self):
        self._config = {}
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as f:
                json_config = json.load(f)

                account_config = json_config.get(constants.ACCOUNTS) or {}

                account_dict = {}
                for key, data in account_config.items():
                    consumer_key = data.get(constants.CONSUMER_KEY)
                    consumer_secret = data.get(constants.CONSUMER_SECRET)
                    access_token = data.get(constants.ACCESS_TOKEN)
                    access_token_secret = data.get(constants.ACCESS_TOKEN_SECRET)
                    is_main_account = data.get(constants.IS_MAIN_ACCOUNT) or False
                    is_dev_account = data.get(constants.IS_DEV_ACCOUNT) or False

                    account = accounts.Account(consumer_key, consumer_secret, access_token, access_token_secret, is_main_account, is_dev_account)
                    account_dict[key] = account

                self._config[constants.ACCOUNTS] = account_dict

    def save(self):
        json_account_config = {}
        for account in self.account_config:
            json_account_config[account] = self.account_config[account].to_json()

        json_config = {}
        json_config[constants.ACCOUNTS] = json_account_config

        if not os.path.isdir(os.path.dirname(constants.CONFIG_FILE)):
            os.makedirs(os.path.dirname(constants.CONFIG_FILE))

        with open(constants.CONFIG_FILE, 'w') as f:
            json.dump(json_config, f, indent=4, sort_keys=True)

