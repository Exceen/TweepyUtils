from pkg_resources import Requirement, resource_filename
import os.path
import config

#### ADDITIONAL FILES ####

CONFIG_PATH = resource_filename(Requirement.parse('tweepyutils'), 'tweepyutils-data')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'tweepyutils_config.json')

config = config.Config(CONFIG_FILE)

#### CONFIG KEYS ####

ACCOUNTS = 'accounts'

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
ACCESS_TOKEN = 'access_token'
ACCESS_TOKEN_SECRET = 'access_token_secret'
IS_MAIN_ACCOUNT = 'is_main_account'
IS_DM_ACCOUNT = 'is_dm_account'

