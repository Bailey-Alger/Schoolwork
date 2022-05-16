def login(database, username, password):
    for key, value in database.items():
        if username == key and password == value:
            print('Welcome,', username)
            return username
        elif username == key and password != value:
            print('Password incorrect.')
            return ''
    print('Username not found.')
    return ''


def register(database, username):
    if username in database.keys():
        print('Username already registered.')
        return ''
    else:
        print('Username registed.')
        return username
