from donations_pkg import user
from donations_pkg.homepage import show_donations, show_homepage, donate
from donations_pkg.user import login, register

database = {'admin': 'password123'}
donations = []
authorized_user = ''

while True:
    show_homepage()
    if authorized_user == '':
        print('You must be logged in to donate.')
    else:
        print('Logged in as:', authorized_user)

    choice = input('Choose an option: ')

    if choice == '1':
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = login(database, username, password)
        continue
    elif choice == '2':
        username = input('Enter username: ')
        password = input('Enter password: ')
        authorized_user = register(database, username)
        if authorized_user != '':
            database[username] = password
        continue
    elif choice == '3':
        if authorized_user == '':
            print('You are not logged in.')
            continue
        else:
            donation = donate(authorized_user)
            donations.append(donation)
        continue
    elif choice == '4':
        show_donations(donations)
    elif choice == '5':
        print('Goodbye!')
        quit()
    else:
        continue
