from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


name = input('Enter name to register: ')
pin = input('Enter PIN: ')
balance = 0
print(name + ' has been registed with a starting balance of $' + str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print('LOGIN')
    name_entered = input('Enter Name: ')
    pin_entered = input('Enter PIN: ')
    if name_entered == name and pin_entered == pin:
        print('Login successful!')
        break
    else:
        print('Invalid Credentials!')

while True:
    atm_menu(name)  # name should be user?
    option = input('Choose an option: ')
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == '4':
        account.logout(name)
        break
    else:
        continue
