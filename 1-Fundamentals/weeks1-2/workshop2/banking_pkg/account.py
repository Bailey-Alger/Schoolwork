def show_balance(balance):
    print('Current Balance: $' + str(balance))


def deposit(balance):
    amount = float(input('Enter amount to deposit: '))
    return balance + amount


def withdraw(balance):
    amount = float(input('Enter amount to windraw: '))
    return balance - amount


def logout(name):
    print('Goodbye ' + name + '!')
