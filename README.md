Tweepy Utils
============

### Usage ###

```
from tweepyutils import accounts
from tweepyutils import followings
```

### Accounts ###

```
accounts.get_available_account_names()
accounts.get_account(name)

accounts.get_main_account()
accounts.get_secondary_account()
```

### Retrieving tweepy.API object ###

```
account = accounts.get_account('Username') # username as defined in the config file
api = account.api

# or

accounts.get_api('Username') # directly retrieves the tweepyAPI-object
```

### Followings ###

```TODO```

### TODO ###

- [x] Store multiple accounts
- [x] Manage accounts via an add/remove script
- [x] Retrieve various data about followers (new followers, unfollowers, ...)
- [ ] Update README
- [ ] Whatever