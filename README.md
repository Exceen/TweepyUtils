Tweepy Utils
============

### Usage ###

```
from tweepyutils import accounts
```

### Accounts ###

```
accounts.get_account(name)
accounts.get_main_account()
accounts.get_secondary_account()
accounts.get_available_accounts()
```

### Retrieving tweepy.API object ###

```
account = accounts.get_account('Username') # username as defined in the config file
api = account.api

# or

accounts.get_api('Username') # directly retrieves the tweepyAPI-object
```

### TODO ###

- [x] Store multiple accounts
- [ ] Manage accounts via an add/remove script
- [ ] Retrieve various data about followers (new followers, unfollowers, ...)

