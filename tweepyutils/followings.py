from tweepyutils import accounts, constants
from os import makedirs, path

DATABASE_FILE = path.join(constants.CONFIG_PATH, 'followers.db')

class Followings(object):
    def __init__(self, account):
        self.account = account
        self._screen_name = self.account.api.me().screen_name
        
    def __get_friends_file(self):
        return path.join(constants.CONFIG_PATH, self._screen_name + '_friends')

    def __get_followers_file(self):
        return path.join(constants.CONFIG_PATH, self._screen_name + '_followers')

    def get_username_from_database(self, user_id):
        db = []
        if path.exists(DATABASE_FILE):
            db = [line.strip() for line in open(DATABASE_FILE, 'r')]
        for record in db:
            if str(user_id) in record:
                return record.split('|')[-1]
        return 'Unkown User'

    def get_username(self, user_id):
        username = self.get_username_from_database(user_id)
        if username == None:
            try:
                username = self.account.api.get_user(user_id).screen_name
            except Exception, e:
                pass
        return username

    def get_friends_from_database(self):
        if path.exists(self.__get_friends_file()):
            return [line.strip() for line in open(self.__get_friends_file())]
        else:
            return self.account.friends

    def get_followers_from_database(self):
        if path.exists(self.__get_followers_file()):
            return [line.strip() for line in open(self.__get_followers_file())]
        else:
            return self.account.followers

    def update_database(self, user_id_list):
        db = []
        if path.exists(DATABASE_FILE):
            db = [line.strip() for line in open(DATABASE_FILE, 'r')]

        user_id_list.append(self._screen_name)
        for user_id in user_id_list:
            user_id = str(user_id)
            if not any(user_id in data for data in db):
                try:
                    data_set = user_id + '|' + str(self.account.api.get_user(user_id).screen_name)
                    db.append(data_set)
                except tweepy.error.TweepError, err:
                    continue

        with open(DATABASE_FILE, 'w') as f:
            [f.write('%s\n' % item) for item in db]

    def save_followings(self):
        if not path.exists(constants.CONFIG_PATH):
            makedirs(constants.CONFIG_PATH)

        with open(self.__get_friends_file(), 'w') as f:
            [f.write('%s\n' % item) for item in self.account.friends]
        with open(self.__get_followers_file(), 'w') as f:
            [f.write('%s\n' % item) for item in self.account.followers]
        self.update_database(self.account.friends + self.account.followers)

